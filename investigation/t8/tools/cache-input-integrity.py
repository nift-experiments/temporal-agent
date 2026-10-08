"""Corrupted/absent transient products must repair to the independently built publication."""
from pathlib import Path
import subprocess,hashlib,json,os
root=Path(__file__).resolve().parent.parent;node=root/'toolchain/node-v24.21.0-linux-x64/bin/node';env={**os.environ,'PATH':str(root/'toolchain/frozen-bin')+':'+os.environ['PATH']};results=[]
def manifest(repo):return {str(p.relative_to(repo/'public')):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((repo/'public').rglob('*')) if p.is_file()}
def build(repo,args,log):
 with log.open('w') as f:subprocess.run([str(node),'tools/publish.cjs',*args],cwd=repo,env=env,stdout=f,stderr=subprocess.STDOUT,check=True)
for name in ['temporal','temporal-agent']:
 repo=root.parent/name;out=root/'runs'/('t8-cache-integrity-'+name);out.mkdir(exist_ok=False)
 build(repo,['--force'],out/'independent-baseline.log');baseline=manifest(repo)
 faults=[('body',repo/'.cache/rendered/cli.html'),('shell',repo/'.cache/shell/cli.prefix.html'),('browser',next((repo/'.cache/bundle/browser').glob('client-*.js'))),('server',repo/'.cache/bundle/server/server.cjs'),('download',repo/'public/cli/setup-cli.md')]
 if name=='temporal':faults.append(('compiled-mdx',repo/'.cache/mdx/docs/cli/setup-cli.mdx.jsx'))
 for case,file in faults:
  file.write_bytes(b'TEMPORAL_CORRUPTED_TRANSIENT_PRODUCT\n');build(repo,[],out/(case+'-repair.log'));now=manifest(repo);diff=[p for p in sorted(set(baseline)|set(now)) if baseline.get(p)!=now.get(p)];result={'project':name,'fault':case,'injected_file':str(file.relative_to(repo)),'normal_repaired_to_independent_publication':not diff,'differences':diff};results.append(result);print(result,flush=True)
  if diff:raise RuntimeError('Transient corruption changed publication')
(root/'runs/t8-cache-input-integrity.json').write_text(json.dumps(results,indent=2)+'\n')
