"""
Handler for Organisation/Institution submissions.
Wraps institution.py and returns EMD-style {filepath: data} dict.
"""
import os
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import institution

FOLDER = 'organisation'


def run(parsed_issue, issue, dry_run=False):
    result = institution.run(parsed_issue, issue, dry_run)
    if result is None:
        return None

    data, _ = result

    data_id = data.get('@id', '')
    file_path = os.path.join(FOLDER, f"{data_id}.json")

    collab_str = parsed_issue.get('additional_collaborators', parsed_issue.get('collaborators', ''))
    contributors = [c.strip() for c in collab_str.split(',') if c.strip()] if collab_str else []

    return {
        file_path:       data,
        '_author':       issue.get('author'),
        '_contributors': contributors,
        '_make_pull':    True,
    }


def update(files_to_write, parsed_issue, issue, dry_run=False):
    file_path = next((p for p in files_to_write if not p.startswith('_')), None)
    if not file_path:
        return files_to_write

    data = files_to_write[file_path]
    updated = institution.update(data, parsed_issue, issue, dry_run)
    files_to_write[file_path] = updated
    return files_to_write
