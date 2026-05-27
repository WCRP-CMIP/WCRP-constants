"""
Generic handler for simple WCRP CV entries.

Each CV-specific script imports this and calls run()/update() with
its own folder and type list.
"""

import os
import json

IGNORE = {
    'issue_kind', 'issue_category', 'additional_collaborators',
    'collaborators', 'header',
}


def _clean(value):
    if isinstance(value, str):
        v = value.strip()
        return None if v.lower() in ('_no response_', 'none', 'not specified', '') else v
    return value


def run(parsed_issue, issue, folder, types, dry_run=False):
    prefix = "[DRY RUN] " if dry_run else ""

    validation_key = (
        parsed_issue.get('validation_key') or
        parsed_issue.get('label') or ''
    ).strip()

    if not validation_key:
        print(f"{prefix}❌ No validation_key provided")
        return None

    data_id = validation_key.lower().replace(' ', '-').replace('_', '-')

    data = {
        "@context":       "_context",
        "@id":            data_id,
        "@type":          types,
        "validation_key": validation_key,
    }

    ui_label = _clean(parsed_issue.get('ui_label') or parsed_issue.get('long_label') or '')
    if ui_label:
        data['ui_label'] = ui_label

    description = _clean(parsed_issue.get('description') or '')
    if description:
        data['description'] = description

    for k, v in parsed_issue.items():
        if k in IGNORE or k in ('validation_key', 'ui_label', 'long_label', 'description', 'label'):
            continue
        cleaned = _clean(v)
        if cleaned is not None:
            data[k] = cleaned

    file_path = os.path.join(folder, f"{data_id}.json")

    collab_str = parsed_issue.get('additional_collaborators', parsed_issue.get('collaborators', ''))
    contributors = [c.strip() for c in collab_str.split(',') if c.strip()] if collab_str else []

    print(f"{prefix}→ {file_path}")
    print(json.dumps(data, indent=2, ensure_ascii=False))

    return {
        file_path:       data,
        '_author':       issue.get('author'),
        '_contributors': contributors,
        '_make_pull':    True,
    }


def update(files_to_write, parsed_issue, issue, dry_run=False):
    for file_path, data in files_to_write.items():
        if file_path.startswith('_'):
            continue
        print(f"✓ {file_path} ready")
    return files_to_write
