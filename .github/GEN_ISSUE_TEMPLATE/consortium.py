# Consortium Template Data
import cmipld
from cmipld.utils.ldparse import name_extract

try:
    org = name_extract(cmipld.get('constants:organisation/graph.jsonld', depth=0))
    inst = [f"{k} : {v.get('ui_label','')}" for k, v in org.items() if 'ror' in v]
except Exception as e:
    print(f"  ⚠ Could not fetch institutions from LDR: {e}")
    inst = []

DATA = {
    'issue_kind': ['New', 'Modify'],
    'institutions': inst
}
