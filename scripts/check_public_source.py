"""Fail on accidental local artifacts and invalid static download types."""
from pathlib import Path
root=Path(__file__).resolve().parents[1]
ignored={'node_modules','.git','build','.docusaurus','.tmp','sdk-source'}
fail=[]
for path in root.rglob('*'):
    rel=path.relative_to(root)
    if any(x in ignored for x in rel.parts): continue
    if path.is_symlink(): fail.append(str(rel))
    if not path.is_file(): continue
    if path.name.startswith('.env') or path.name=='.npmrc' or path.suffix in {'.pem','.key','.pyc','.log','.db','.sqlite3'} or '__pycache__' in rel.parts:
        fail.append(str(rel))
    if rel.parts[0]=='static' and path.suffix not in {'.svg','.py','.sh'} and path.name!='.nojekyll': fail.append(str(rel))
if fail: raise SystemExit('Unexpected public artifacts: '+', '.join(fail))
print('Public artifact boundary OK (not a substitute for secret scanning).')
