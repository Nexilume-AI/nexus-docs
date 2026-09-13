"""Retain known findings; fail closed on new advisories or a failed audit."""
import json
import subprocess
import os

known = {'https://github.com/advisories/GHSA-w3rx-r6r6-pgpr',
         'https://github.com/advisories/GHSA-5p2g-fcmc-qvqq'}
result = subprocess.run(['npm.cmd' if os.name == 'nt' else 'npm', 'audit', '--json'],
                        capture_output=True, text=True, timeout=180)
data = json.loads(result.stdout)
if result.returncode not in (0, 1) or data.get('error') or 'vulnerabilities' not in data:
    raise SystemExit('Dependency audit unavailable; review failed.')
unknown=[]
for name, item in data['vulnerabilities'].items():
    if item.get('severity') == 'critical': unknown.append(name)
    for via in item.get('via', []):
        if isinstance(via, dict) and via.get('url') not in known:
            unknown.append(via.get('url', name))
print(json.dumps(data['metadata']['vulnerabilities']))
if unknown: raise SystemExit('New dependency advisory requires review: '+', '.join(unknown))
if data['vulnerabilities']:
    print('KNOWN RISK REMAINS: image-size parser DoS; see SECURITY.md and run check:security.')
