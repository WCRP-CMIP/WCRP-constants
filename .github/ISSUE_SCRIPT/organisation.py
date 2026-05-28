"""
Organisation/Institution handler.
Fetches full ROR data and produces a complete institution record.
No imports from other files in this directory.
"""

import os
import json
from difflib import SequenceMatcher


# ── ROR fetch (inlined from update_ror to avoid same-folder imports) ──────────

def _get_ror_data(ror_id, acronym, types):
    """
    Fetch full institution data from ROR API v2.
    Returns a complete structured dict matching the institution JSON-LD schema.
    """
    import cmipld
    from cmipld.utils.jsontools import sort_json_keys

    url = f'https://api.ror.org/v2/organizations/{ror_id}'
    ror  = cmipld.utils.read_url(url)

    assert ror, f"No ROR data found for {ror_id} at {url}"

    cmip_id = acronym.lower().replace('_', '-').replace(' ', '-')

    names        = ror.get('names', [])
    display_name = next(
        (n['value'] for n in names if 'ror_display' in n.get('types', [])),
        names[0]['value'] if names else None
    )
    loc = ror.get('locations', [{}])[0].get('geonames_details', {})

    result = {
        "@context":       "_context",
        "@id":            cmip_id,
        "@type":          types,
        "validation_key": acronym,
        "ror":            ror['id'].split('/')[-1],
        "ui_label":       display_name,
        "url":            [l['value'] for l in ror.get('links', [])],
        "established":    ror.get('established'),
        "kind":           ror.get('types', [None])[0],
        "labels":         [n['value'] for n in names if 'label'   in n.get('types', [])],
        "aliases":        [n['value'] for n in names if 'alias'   in n.get('types', [])],
        "acronyms":       [n['value'] for n in names if 'acronym' in n.get('types', [])],
        "location": [{
            "@id":                       f"universal:location/{ror['id'].split('/')[-1]}",
            "@type":                     "wcrp:location",
            "lat":                       loc.get('lat'),
            "lng":                       loc.get('lng'),
            "name":                      loc.get('name'),
            "country_code":              loc.get('country_code'),
            "country_name":              loc.get('country_name'),
            "country_subdivision_code":  loc.get('country_subdivision_code'),
            "country_subdivision_name":  loc.get('country_subdivision_name'),
            "continent_code":            loc.get('continent_code'),
            "continent_name":            loc.get('continent_name'),
        }],
    }

    return sort_json_keys(result)


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


# ── GitHub helpers ────────────────────────────────────────────────────────────

def _gh_comment(issue_number, body):
    escaped = body.replace("'", "'\"'\"'")
    os.popen(f"gh issue comment {issue_number} --body '{escaped}'").read()


def _gh_label(issue_number, label):
    os.popen(f'gh issue edit {issue_number} --add-label "{label}"').read()


# ── Handler ───────────────────────────────────────────────────────────────────

def run(parsed_issue, issue, dry_run=False):
    prefix       = "[DRY RUN] " if dry_run else ""
    issue_number = issue.get('number', os.environ.get('ISSUE_NUMBER', ''))
    folder       = issue.get('folder', 'organisation')
    types        = issue.get('types', ['wcrp:organisation', 'wcrp:institution'])

    warnings = []
    ror_name = None
    ranking  = None

    acronym    = (parsed_issue.get('acronym') or parsed_issue.get('label') or '').strip()
    full_name  = (parsed_issue.get('full_name_of_the_organisation') or
                  parsed_issue.get('long_label') or '').strip()
    ror_id     = (parsed_issue.get('ror') or parsed_issue.get('description') or '').strip()
    collab_str = (parsed_issue.get('additional_collaborators') or
                  parsed_issue.get('collaborators') or '')
    contributors = [c.strip() for c in collab_str.split(',') if c.strip()]

    if not acronym:
        print(f"{prefix}❌  No acronym provided")
        return None

    data_id   = acronym.lower().replace(' ', '-').replace('_', '-')
    ror_empty = not ror_id or ror_id.lower() in ('pending', 'none', '')

    print(f"{prefix}Acronym={acronym}  @id={data_id}  folder={folder}  ROR={ror_id or 'pending'}")

    if not ror_empty:
        try:
            data     = _get_ror_data(ror_id, acronym, types)
            ror_name = data.get('ui_label', '')

            if full_name and ror_name:
                ranking = SequenceMatcher(None, full_name.lower(), ror_name.lower()).ratio() * 100
                print(f"{prefix}Name similarity: {ranking:.1f}%  ({full_name!r} vs {ror_name!r})")
                if ranking < 80:
                    warnings.append(
                        f"Low name similarity ({ranking:.1f}%): '{full_name}' vs '{ror_name}'"
                    )

        except Exception as e:
            warnings.append(f"ROR fetch failed: {e}")
            print(f"{prefix}⚠  {warnings[-1]}")
            data = _basic_data(data_id, acronym, full_name, ror_id, types)
    else:
        warnings.append("No ROR ID provided — institution data is incomplete")
        data = _basic_data(data_id, acronym, full_name, None, types)

    # Always enforce the template-declared @type
    data['@type'] = types

    if not dry_run and issue_number:
        _post_summary(issue_number, acronym, full_name, ror_id, ror_name, ranking, warnings)
        if warnings:
            _gh_label(issue_number, 'needs-review')

    print(json.dumps(data, indent=2, ensure_ascii=False))

    return {
        f"{folder}/{data_id}.json": data,
        '_author':       issue.get('author'),
        '_contributors': contributors,
        '_make_pull':    True,
    }


def update(files, parsed_issue, issue, dry_run=False):
    """Re-enrich from ROR if location data is missing."""
    prefix = "[DRY RUN] " if dry_run else ""
    types  = issue.get('types', ['wcrp:organisation', 'wcrp:institution'])

    file_path = next((p for p in files if not p.startswith('_')), None)
    if not file_path:
        return files

    data   = files[file_path]
    ror_id = (parsed_issue.get('ror') or parsed_issue.get('description') or '').strip()

    if data.get('location'):
        print(f"{prefix}Already has location data — skipping ROR re-fetch")
        return files

    if not ror_id or ror_id.lower() in ('pending', 'none', ''):
        print(f"{prefix}No ROR ID — skipping enrichment")
        return files

    try:
        acronym  = data.get('validation_key', data.get('@id', ''))
        enriched = _get_ror_data(ror_id, acronym, types)
        files[file_path] = enriched
        print(f"{prefix}✓ ROR data merged — {len(enriched)} fields")
    except Exception as e:
        print(f"{prefix}⚠  ROR update failed: {e}")

    return files


# ── Summary comment ───────────────────────────────────────────────────────────

def _post_summary(issue_number, acronym, full_name, ror_id, ror_name, ranking, warnings):
    status = "✅ Passed" if not warnings else "⚠️ Needs Review"
    lines  = [
        "## Institution Validation Summary\n",
        "| Field | Value |",
        "|-------|-------|",
        f"| **Status** | {status} |",
        f"| **Acronym** | `{acronym}` |",
        f"| **Full Name (provided)** | {full_name or '_not provided_'} |",
        f"| **Full Name (from ROR)** | {ror_name or '_not available_'} |",
        f"| **ROR ID** | `{ror_id or 'pending'}` |",
        f"| **Name similarity** | {f'{ranking:.1f}%' if ranking is not None else '_n/a_'} |",
    ]
    if warnings:
        lines += ["\n### ⚠️ Warnings\n"] + [f"- {w}" for w in warnings]
    _gh_comment(issue_number, "\n".join(lines))
