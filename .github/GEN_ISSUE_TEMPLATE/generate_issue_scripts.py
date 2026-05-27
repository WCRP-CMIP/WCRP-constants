#!/usr/bin/env python3
"""
Generate ISSUE_SCRIPT handlers for all CV types in _config.json.
Run from: .github/GEN_ISSUE_TEMPLATE/
"""
import json
from pathlib import Path

config_path = Path(__file__).parent / '_config.json'
with open(config_path) as f:
    config = json.load(f)

issue_script_dir = Path(__file__).parent.parent / 'ISSUE_SCRIPT'

# Templates with custom handlers — skip generation
CUSTOM = {'organisation', 'institution'}
# Special folder/type overrides
SPECIAL = {
    'consortium': ('organisation', ['wcrp:organisation', 'wcrp:consortium']),
}

generated = 0
for template_name in config['template_order']:
    if template_name in CUSTOM:
        print(f"⊘ {template_name} — custom handler exists")
        continue

    out_path = issue_script_dir / f'{template_name}.py'

    if out_path.exists():
        print(f"✓ {template_name}.py already exists")
        continue

    folder = config['folder_mapping'].get(template_name, template_name)
    title  = template_name.replace('_', ' ').title()
    types  = [f'wcrp:{template_name}']

    if template_name in SPECIAL:
        folder, types = SPECIAL[template_name]

    type_str = json.dumps(types)

    content = f'''"""
Handler for {title} submissions.
Auto-generated — edit _base.py for shared logic.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import _base

FOLDER = {repr(folder)}
TYPES  = {type_str}


def run(parsed_issue, issue, dry_run=False):
    return _base.run(parsed_issue, issue, FOLDER, TYPES, dry_run)


def update(files_to_write, parsed_issue, issue, dry_run=False):
    return _base.update(files_to_write, parsed_issue, issue, dry_run)
'''

    out_path.write_text(content)
    print(f"✓ Created {template_name}.py  →  {folder}/")
    generated += 1

print(f"\n✅ Generated {generated} handlers")
