from pathlib import Path
import subprocess,json,hashlib,os
root=Path(__file__).resolve().parent.parent
for project in ['temporal','temporal-agent']:
 repo=root.parent/project
 def manifest():return {str(p.relative_to(repo/'public')):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((repo/'public').rglob('*')) if p.is_file()}
 previous=manifest()
 for mode in ['force','unchanged']:
  args=['python3',str(root/'tools/measure-publication.py'),'--project',project,'--label','t8-cache-v2-probe-'+project+'-'+mode]
  if mode=='force':args.append('--force')
  subprocess.run(args,check=True)
  now=manifest();diff=[p for p in sorted(set(previous)|set(now)) if previous.get(p)!=now.get(p)]
  # New hashed JS graph names are expected after route-context aliasing; all semantic parity is rechecked separately.
  if mode=='unchanged':
   result={'project':project,'unchanged_equals_independent_forced':not diff,'differences':diff};(root/'runs'/('t8-cache-v2-probe-'+project+'-equality.json')).write_text(json.dumps(result,indent=2)+'\n');print(result,flush=True)
   if diff:raise RuntimeError('Cached publication differs from forced recomputation')
  previous=now
