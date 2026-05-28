#!/usr/bin/env python3
"""
Direct issue processor — called by new-issue.yml.

Routing: issue label -> GEN_ISSUE_TEMPLATE/{label}.json -> issue_category
         -> ISSUE_SCRIPT/{issue_category}.py
         (template filename == script filename, no indirection)
"""

import os
import sys
import json
import re
import subprocess
from pathlib import Path

ISSUE_SCRIPT_DIR  = Path(__file__).parent
REPO_ROOT         = ISSUE_SCRIPT_DIR.parent.parent
GEN_TEMPLATE_DIR  = REPO_ROOT / '.github' / 'GEN_ISSUE_TEMPLATE'


def load_template_registry():
    registry = {}
    for path in GEN_TEMPLATE_DIR.glob('*.json'):
        if path.name.startswith('_'):
            continue
        try:
            meta = json.loads(path.read_text())
        except Exception:
            continue
        category = meta.get('issue_category') or path.stem
        handler  = ISSUE_SCRIPT_DIR / f"{category}.py"
        if not handler.exists():
            continue
        folder = meta.get('folder_tag') or category
        types  = meta.get('types') or [f'wcrp:{category}']
        registry[category] = {
            'handler': handler,
            'folder':  folder,
            'types':   types,
        }
    return registry


def find_handler(labels, registry):
    for label in labels:
        # labels may contain hyphens; registry keys use underscores
        key = label.replace('-', '_')
        if key in registry:
            return key, registry[key]
    return None, None


def load_handler(path):
    """
    Execute handler file in an isolated namespace.
    Avoids sys.path pollution (e.g. calendar.py shadowing the built-in).
    """
    namespace = {
        '__file__':     str(path),
        '__name__':     'handler_module',
        '__builtins__': __builtins__,
    }
    sys.path.insert(0, str(ISSUE_SCRIPT_DIR))
    try:
        with open(path) as f:
            exec(f.read(), namespace)
    finally:
        sys.path.pop(0)

    class Handler:
        @staticmethod
        def run(*args, **kwargs):
            return namespace['run'](*args, **kwargs)
        @staticmethod
        def update(*args, **kwargs):
            return namespace['update'](*args, **kwargs)

    return Handler()


def parse_issue_body(body):
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


def gh(*args):
    return subprocess.run(['gh', *args], capture_output=True, text=True)


def git(cmd, check=True):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if check and r.returncode != 0:
        print(f"git error: {r.stderr.strip()}")
        sys.exit(1)
    return r.stdout.strip()


def main():
    issue_number = os.environ.get('ISSUE_NUMBER', '').strip()
    if not issue_number:
        print("ERROR: ISSUE_NUMBER not set")
        sys.exit(1)

    r = gh('issue', 'view', issue_number,
           '--json', 'body,labels,author,createdAt,url')
    if r.returncode != 0:
        print(f"ERROR: could not fetch issue #{issue_number}: {r.stderr.strip()}")
        sys.exit(1)

    issue_data = json.loads(r.stdout)
    labels  = [l['name'] for l in issue_data.get('labels', [])]
    author  = issue_data.get('author', {}).get('login', '')

    print(f"Issue #{issue_number}  labels={labels}  author={author}")

    registry = load_template_registry()
    handler_name, meta = find_handler(labels, registry)

    if not meta:
        print(f"No handler found for labels {labels} — skipping")
        sys.exit(0)

    print(f"Template → {handler_name}.py  folder={meta['folder']}  types={meta['types']}")

    parsed = parse_issue_body(issue_data.get('body', ''))
    print(f"Fields: {list(parsed.keys())}")

    issue_meta = {
        'author':     author,
        'number':     issue_number,
        'url':        issue_data.get('url', ''),
        'labels':     labels,
        'created_at': issue_data.get('createdAt', ''),
        'folder':     meta['folder'],
        'types':      meta['types'],
        'category':   handler_name,
    }

    handler = load_handler(meta['handler'])
    files   = handler.run(parsed, issue_meta)

    if files is None:
        print("Handler run() returned None — validation failed")
        sys.exit(1)

    files = handler.update(files, parsed, issue_meta)

    # Write files
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
        print("No files written")
        sys.exit(1)

    if not files.get('_make_pull', True):
        sys.exit(0)

    # Branch + PR targeting src-data
    branch = f"issue_{handler_name}_{issue_number}"
    git("git config user.name 'cmip-ipo'")
    git("git config user.email 'actions@wcrp-cmip.org'")
    git("git fetch origin src-data 2>/dev/null || true", check=False)
    git(f"git fetch origin {branch} 2>/dev/null || true", check=False)

    # Reset onto existing remote branch, or create fresh from src-data
    branch_exists = git(f"git ls-remote --heads origin {branch}", check=False).strip()
    if branch_exists:
        git(f"git checkout -B {branch} origin/{branch}")
    else:
        git(f"git checkout -b {branch} origin/src-data 2>/dev/null || git checkout -b {branch}", check=False)

    for fp in written:
        git(f"git add '{REPO_ROOT / fp}'")

    git(f'git commit -m "Add {handler_name} from issue #{issue_number}" --allow-empty')
    git(f"git push --force-with-lease origin {branch}")

    contributors = files.get('_contributors', [])
    pr_body = f"Closes #{issue_number}\n\nSubmitted by @{author}"
    if contributors:
        pr_body += f"\nContributors: {', '.join('@' + c for c in contributors)}"

    # Create PR if it doesn't already exist
    existing_pr = gh('pr', 'view', branch, '--json', 'number', '-q', '.number')
    if existing_pr.returncode != 0:
        gh('pr', 'create',
           '--title', f"Add {handler_name} (Issue #{issue_number})",
           '--body',  pr_body,
           '--head',  branch,
           '--base',  'src-data')
    else:
        print(f"PR already exists for {branch} — updated with force push")


if __name__ == '__main__':
    main()
