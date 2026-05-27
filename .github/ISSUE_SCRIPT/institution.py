"""
Institution Issue Handler — custom logic for ROR lookup.
Folder and types come from issue_meta (driven by template's folder_tag / types
in the .json file), so the same script can be reused if folder ever changes.
"""

import os
import sys
import json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import update_ror


def similarity(a, b):
    from difflib import SequenceMatcher
    if not a or not b:
        return 0
    return SequenceMatcher(None, a.lower(), b.lower()).ratio() * 100


def gh_comment(issue_number, body):
    escaped = body.replace("'", "'\"'\"'")
    os.popen(f"gh issue comment {issue_number} --body '{escaped}'").read()


def gh_label(issue_number, label):
    os.popen(f'gh issue edit {issue_number} --add-label "{label}"').read()


def run(parsed_issue, issue, dry_run=False):
    prefix = "[DRY RUN] " if dry_run else ""
    issue_number = issue.get('number', os.environ.get('ISSUE_NUMBER', ''))
    folder = issue.get('folder', 'organisation')
    types  = issue.get('types', ['wcrp:organisation', 'wcrp:institution'])

    warnings = []
    ranking  = None
    ror_name = None

    acronym   = (parsed_issue.get('acronym') or parsed_issue.get('label') or '').strip()
    full_name = (parsed_issue.get('full_name_of_the_organisation') or
                 parsed_issue.get('long_label') or '').strip()
    ror_id    = (parsed_issue.get('ror') or parsed_issue.get('description') or '').strip()
    collab_str = (parsed_issue.get('additional_collaborators') or
                  parsed_issue.get('collaborators') or '')
    contributors = [c.strip() for c in collab_str.split(',') if c.strip()]

    if not acronym:
        print(f"{prefix}❌ No acronym provided")
        return None

    data_id = acronym.lower().replace(' ', '-').replace('_', '-')
    print(f"{prefix}Acronym={acronym}  @id={data_id}  folder={folder}  ROR={ror_id or 'pending'}")

    ror_empty = not ror_id or ror_id.lower() in ('pending', 'none', '')

    if not ror_empty:
        try:
            data = update_ror.get_institution(ror_id, acronym)
            ror_name = data.get('ui_label', '')
            if full_name and ror_name:
                ranking = similarity(full_name, ror_name)
                print(f"{prefix}Name similarity: {ranking:.1f}%  ({full_name!r} vs {ror_name!r})")
                if ranking < 80:
                    warnings.append(f"Low name similarity ({ranking:.1f}%): '{full_name}' vs '{ror_name}'")
        except Exception as e:
            warnings.append(f"Could not fetch ROR data: {e}")
            print(f"{prefix}⚠ {warnings[-1]}")
            data = _basic_data(data_id, acronym, full_name, ror_id, types)
    else:
        warnings.append("No ROR ID provided — institution data is incomplete")
        data = _basic_data(data_id, acronym, full_name, None, types)

    # Ensure @type reflects the template's declared types
    data['@type'] = types

    if not dry_run and issue_number:
        _post_summary(issue_number, acronym, full_name, ror_id, ror_name, ranking, warnings)
        if warnings:
            gh_label(issue_number, 'needs-review')

    print(json.dumps(data, indent=2, ensure_ascii=False))

    return {
        f"{folder}/{data_id}.json": data,
        '_author':       issue.get('author'),
        '_contributors': contributors,
        '_make_pull':    True,
    }


def update(files, parsed_issue, issue, dry_run=False):
    prefix = "[DRY RUN] " if dry_run else ""

    file_path = next((p for p in files if not p.startswith('_')), None)
    if not file_path:
        return files

    data   = files[file_path]
    ror_id = (parsed_issue.get('ror') or parsed_issue.get('description') or '').strip()

    if data.get('ror') and data.get('location'):
        print(f"{prefix}Already enriched with ROR — skipping update")
        return files

    if not ror_id or ror_id.lower() in ('pending', 'none', ''):
        print(f"{prefix}No ROR ID — skipping enrichment")
        return files

    try:
        ror_data = update_ror.get_institution(ror_id, data.get('validation_key', ''))
        for key, value in ror_data.items():
            if key in ('@context', '@id', '@type'):
                continue
            if value is not None:
                data[key] = value
        print(f"{prefix}ROR data merged")
    except Exception as e:
        print(f"{prefix}⚠ ROR update failed: {e}")

    files[file_path] = data
    return files


def _basic_data(data_id, acronym, full_name, ror_id, types):
    d = {
        "@context":       "_context",
        "@id":            data_id,
        "@type":          types,
        "validation_key": acronym,
    }
    if full_name:
        d['ui_label'] = full_name
    if ror_id and ror_id.lower() not in ('pending', 'none', ''):
        d['ror'] = ror_id
    return d


def _post_summary(issue_number, acronym, full_name, ror_id, ror_name, ranking, warnings):
    status = "✅ Passed" if not warnings else "⚠️ Needs Review"
    lines = [
        "## Institution Validation Summary\n",
        "| Field | Value |",
        "|-------|-------|",
        f"| **Status** | {status} |",
        f"| **Acronym** | `{acronym}` |",
        f"| **Full Name (provided)** | {full_name or '_not provided_'} |",
        f"| **Full Name (from ROR)** | {ror_name or '_not available_'} |",
        f"| **ROR ID** | `{ror_id or 'pending'}` |",
        f"| **Name Similarity** | {f'{ranking:.1f}%' if ranking is not None else '_n/a_'} |",
    ]
    if warnings:
        lines += ["\n### ⚠️ Warnings\n"] + [f"- {w}" for w in warnings]
    gh_comment(issue_number, "\n".join(lines))
