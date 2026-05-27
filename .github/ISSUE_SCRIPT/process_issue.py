#!/usr/bin/env python3
"""
Direct issue processor — called by new-issue.yml.
Reads issue, finds handler from labels, runs it, writes files, creates PR.
"""

import os
import sys
import json
import re
import subprocess
import importlib.util
from pathlib import Path

ISSUE_SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = ISSUE_SCRIPT_DIR.parent.parent  # .github/ISSUE_SCRIPT -> repo root


def parse_issue_body(body):
    """Parse GitHub issue form body (### headers) into a normalised dict."""
    fields = {}
    if not body:
        return fields
    sections = re.split(r'^### (.+)$', body, flags=re.MULTILINE)
    it = iter(sections[1:])
    for header, content in zip(it, it):
        key = (header.strip().lower()
               .replace(' ', '_').replace('/', '_')
               .replace('-', '_').replace('(', '').replace(')', ''))
        value = content.strip()
        if value.lower() in ('_no response_', 'none', ''):
            value = ''
        fields[key] = value
    return fields


def find_handler(labels):
    """Return (label, path) for the first label that has a matching handler."""
    for label in labels:
        path = ISSUE_SCRIPT_DIR / f"{label}.py"
        if path.exists():
            return label, path
    return None, None


def load_handler(path):
    spec = importlib.util.spec_from_file_location("handler", path)
    mod = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(ISSUE_SCRIPT_DIR))
    spec.loader.exec_module(mod)
    return mod


def gh(*args):
    result = subprocess.run(["gh", *args], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"gh error: {result.stderr.strip()}")
    return result


def git(cmd, check=True):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"git error: {result.stderr.strip()}")
        sys.exit(1)
    return result.stdout.strip()


def main():
    issue_number = os.environ.get('ISSUE_NUMBER', '').strip()
    if not issue_number:
        print("ERROR: ISSUE_NUMBER not set")
        sys.exit(1)

    # Fetch issue metadata
    r = gh("issue", "view", issue_number,
           "--json", "body,labels,author,createdAt,url")
    if r.returncode != 0:
        print(f"ERROR: could not fetch issue #{issue_number}")
        sys.exit(1)

    issue_data = json.loads(r.stdout)
    labels   = [l['name'] for l in issue_data.get('labels', [])]
    author   = issue_data.get('author', {}).get('login', '')
    body     = issue_data.get('body', '')

    print(f"Issue #{issue_number}  labels={labels}  author={author}")

    # Find handler
    handler_name, handler_path = find_handler(labels)
    if not handler_path:
        print(f"No handler found for labels {labels} — skipping")
        sys.exit(0)

    print(f"Handler: {handler_name}.py")

    # Parse body
    parsed = parse_issue_body(body)
    print(f"Fields: {list(parsed.keys())}")

    issue_meta = {
        'author':      author,
        'number':      issue_number,
        'url':         issue_data.get('url', ''),
        'labels':      labels,
        'created_at':  issue_data.get('createdAt', ''),
    }

    # Run handler
    handler = load_handler(handler_path)

    files = handler.run(parsed, issue_meta)
    if files is None:
        print("Handler run() returned None — validation failed")
        sys.exit(1)

    files = handler.update(files, parsed, issue_meta)

    # Write files to repo
    written = []
    for file_path, data in files.items():
        if file_path.startswith('_'):
            continue
        out = REPO_ROOT / file_path
        out.parent.mkdir(parents=True, exist_ok=True)
        with open(out, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.write('\n')
        print(f"✓ {file_path}")
        written.append(file_path)

    if not written:
        print("No files written — nothing to PR")
        sys.exit(1)

    if not files.get('_make_pull', True):
        print("_make_pull=False — skipping PR")
        sys.exit(0)

    # Create branch + PR targeting src-data
    branch = f"issue_{handler_name}_{issue_number}"
    git(f"git config user.name 'cmip-ipo'")
    git(f"git config user.email 'actions@wcrp-cmip.org'")

    # Ensure we're on src-data or create branch from it
    git(f"git fetch origin src-data || true", check=False)
    git(f"git checkout -b {branch} origin/src-data 2>/dev/null || git checkout -b {branch}", check=False)

    for fp in written:
        git(f"git add {REPO_ROOT / fp}")

    git(f'git commit -m "Add {handler_name} from issue #{issue_number}"')
    git(f"git push origin {branch}")

    contributors = files.get('_contributors', [])
    body_lines = [f"Closes #{issue_number}", f"\nSubmitted by @{author}"]
    if contributors:
        body_lines.append(f"Contributors: {', '.join('@' + c for c in contributors)}")

    gh("pr", "create",
       "--title", f"Add {handler_name} (Issue #{issue_number})",
       "--body", "\n".join(body_lines),
       "--head", branch,
       "--base", "src-data")


if __name__ == '__main__':
    main()
