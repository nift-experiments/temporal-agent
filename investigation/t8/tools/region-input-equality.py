"""Real included region reference invalidates its derived count and all consumers."""
from pathlib import Path
import subprocess,hashlib,json,os
root=Path(__file__).resolve().parent.parent;repo=root.parent/'temporal';node=root/'toolchain/node-v24.21.0-linux-x64/bin/node';env={**os.environ,'PATH':str(root/'toolchain/frozen-bin')+':'+os.environ['PATH']};out=root/'runs/t8-region-input-v2';out.mkdir(exist_ok=False);source=repo/'docs/cloud/references/regions/awsregions.md';original=source.read_bytes()
def build(force,label):
 with (out/(label+'.log')).open('w') as log:subprocess.run([str(node),'tools/publish.cjs']+(['--force'] if force else []),cwd=repo,env=env,stdout=log,stderr=subprocess.STDOUT,check=True)
def manifest():return {str(p.relative_to(repo/'public')):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((repo/'public').rglob('*')) if p.is_file()}
try:
 before=json.loads((repo/'.cache/globalData.json').read_text())['cloud-region-counts']['default']['counts']['aws'];source.write_bytes(original+b'\n\n### T8 region reference fixture\n\nTEMPORAL_T8_REGION_SOURCE\n');build(False,'incremental');after=json.loads((repo/'.cache/globalData.json').read_text())['cloud-region-counts']['default']['counts']['aws'];assert after==before+1;incremental=manifest();build(True,'forced');forced=manifest();diff=[p for p in sorted(set(incremental)|set(forced)) if incremental.get(p)!=forced.get(p)];result={'derived_aws_count_before':before,'derived_aws_count_after':after,'incremental_equals_independent_forced':not diff,'differences':diff};(out/'result.json').write_text(json.dumps(result,indent=2)+'\n');print(result,flush=True)
 if diff:raise RuntimeError('Included reference invalidation failed')
finally:
 source.write_bytes(original);build(False,'restore')
