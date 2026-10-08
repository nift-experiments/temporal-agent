from pathlib import Path
import subprocess,os,json
root=Path(__file__).resolve().parent.parent;env={**os.environ,'PATH':str(root/'toolchain/frozen-bin')+':'+str(root/'toolchain/node-v24.21.0-linux-x64/bin')+':'+os.environ['PATH']}
def measure(project,label):subprocess.run(['python3',str(root/'tools/measure-publication.py'),'--project',project,'--label',label],env=env,check=True)
for project in ['upstream','temporal','temporal-agent']:measure(project,'t7-initial-'+project+'-unchanged')
repo=root/'build-work'
for case,file in [('body',repo/'docs/cli/setup-cli.mdx'),('navigation',repo/'sidebars.js')]:
 original=file.read_bytes()
 try:
  if case=='body':changed=original+b'\n\n```text\nTEMPORAL_T7_UPSTREAM_BODY\n```\n'
  else:changed=original.replace(b'label: "Temporal Cloud"',b'label: "Temporal Cloud T7 upstream navigation"').replace(b"label: 'Temporal Cloud'",b"label: 'Temporal Cloud T7 upstream navigation'")
  assert changed!=original;file.write_bytes(changed);measure('upstream','t7-initial-upstream-change-'+case)
 finally:
  file.write_bytes(original);measure('upstream','t7-initial-upstream-restore-'+case)
