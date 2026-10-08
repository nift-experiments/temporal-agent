from pathlib import Path
import subprocess,json
root=Path(__file__).resolve().parent.parent;repo=root/'build-work'
def measure(label):subprocess.run(['python3',str(root/'tools/measure-publication.py'),'--project','upstream','--label',label],check=True,stdout=(root/'runs'/(label+'-driver.log')).open('w'))
results=[]
for case,source in [('body',repo/'docs/cli/setup-cli.mdx'),('navigation',repo/'sidebars.js')]:
 original=source.read_bytes();marker='TEMPORAL_T9_UPSTREAM_'+case.upper()
 try:
  if case=='body':changed=original+b'\n\n```text\n'+marker.encode()+b'\n```\n'
  else:changed=original.replace(b'label: "Temporal Cloud"',('label: "Temporal Cloud '+marker+'"').encode()).replace(b"label: 'Temporal Cloud'",("label: 'Temporal Cloud "+marker+"'").encode())
  assert changed!=original;source.write_bytes(changed);label='t9-upstream-change-'+case;measure(label)
  assert any(marker.encode() in p.read_bytes() for p in (repo/'build').rglob('*.html'))
  results.append({'case':case,'observable_change_verified':True,'measurement':json.loads((root/'runs'/label/'measurement.json').read_text())})
 finally:
  source.write_bytes(original);measure('t9-upstream-restore-'+case)
(root/'runs/t9-upstream-changed-inputs.json').write_text(json.dumps(results,indent=2)+'\n')
