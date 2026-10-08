"""Public checkout gate. Dependency acquisition is outside publication timing."""
from pathlib import Path
import subprocess,os,json,hashlib,time
root=Path(__file__).resolve().parent.parent
out=root/'runs/t9-clean-clones';out.mkdir(exist_ok=False)
node=root/'toolchain/node-v24.21.0-linux-x64/bin/node';yarn=root/'toolchain/yarn/node_modules/.bin/yarn'
env={**os.environ,'PATH':str(root/'toolchain/frozen-bin')+':'+str(node.parent)+':'+os.environ['PATH']}
records=[]
for name in ['temporal','temporal-agent']:
 repo=root/'repro'/name;repo.parent.mkdir(exist_ok=True)
 with (out/(name+'-clone-install.log')).open('w') as f:
  subprocess.run(['git','clone','https://github.com/nift-experiments/'+name+'.git',str(repo)],stdout=f,stderr=subprocess.STDOUT,check=True)
  commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=repo,text=True).strip()
  assert commit==subprocess.check_output(['git','rev-parse','HEAD'],cwd=root.parent/name,text=True).strip()
  t=time.monotonic();subprocess.run([str(yarn),'install','--frozen-lockfile','--ignore-scripts','--non-interactive'],cwd=repo,env=env,stdout=f,stderr=subprocess.STDOUT,check=True);install=time.monotonic()-t
 assert not (repo/'node_modules').is_symlink()
 with (out/(name+'-publication.log')).open('w') as f:
  t=time.monotonic();subprocess.run([str(node),'tools/publish.cjs'],cwd=repo,env=env,stdout=f,stderr=subprocess.STDOUT,check=True);wall=time.monotonic()-t
 assert not subprocess.check_output(['git','status','--porcelain'],cwd=repo,text=True).strip()
 def manifest(base):return {str(p.relative_to(base)):hashlib.sha256(p.read_bytes()).hexdigest() for p in base.rglob('*') if p.is_file()}
 clean=manifest(repo/'public');working=manifest(root.parent/name/'public');diff=[p for p in sorted(set(clean)|set(working)) if clean.get(p)!=working.get(p)]
 records.append({'project':name,'public_clone_commit':commit,'dependency_install_seconds_outside_publication':install,'clean_normal_publication_seconds_diagnostic':wall,'files':len(clean),'byte_manifest_equals_working_publication':not diff,'differences':diff,'source_clean':True,'node_modules_is_symlink':False})
 (out/'result.json').write_text(json.dumps(records,indent=2)+'\n');print(records[-1],flush=True)
 if diff:raise RuntimeError('Fresh public clone publication differs')
