"""
Handler for Organisation/Institution submissions.
Delegates directly to institution.py.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from institution import run, update
