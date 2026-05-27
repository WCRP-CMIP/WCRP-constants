"""Folder and types come from issue_meta via process_issue.py."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from _base import run, update
