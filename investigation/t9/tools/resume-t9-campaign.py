"""Serialized five-sample complete publication campaign; no dependency acquisition."""
from pathlib import Path
import subprocess,json,shutil,os,hashlib
root=Path(__file__).resolve().parent.parent
projects=['upstream','temporal','temporal-agent'];samples=5
manifest=json.loads((root/'runs/t9-campaign-index.json').read_text())
for scenario in ['warm-full','fresh-app','unchanged']:
 for sample in range(1,samples+1):
  offset=(sample-1)%3;order=projects[offset:]+projects[:offset]
  for project in order:
   if any(r['project']==project and r['scenario']==scenario and r['sample']==sample for r in manifest['runs']):continue
   preparation=[]
   if scenario=='fresh-app':
    cwd=root/'build-work' if project=='upstream' else root.parent/project
    directories=['.docusaurus','build','node_modules/.cache'] if project=='upstream' else ['.cache','public','.nift/public']
    for directory in directories:
     target=cwd/directory;shutil.rmtree(target,ignore_errors=True);preparation.append(str(target))
   label='t9-'+project+'-'+scenario+'-'+str(sample)
   if (root/'runs'/label).exists():label+='-retry1'
   args=['python3',str(root/'tools/measure-publication.py'),'--project',project,'--label',label]
   if project!='upstream' and scenario!='unchanged':args.append('--force')
   subprocess.run(args,check=True)
   measurement=json.loads((root/'runs'/label/'measurement.json').read_text())
   if project=='upstream':
    stats=root/'build-work/build/.og-image-stats.json'
    measurement['og_stats']=json.loads(stats.read_text()) if stats.exists() else None
    (root/'runs'/label/'measurement.json').write_text(json.dumps(measurement,indent=2)+'\n')
   manifest['runs'].append({'label':label,'project':project,'scenario':scenario,'sample':sample,'preparation_outside_timing':preparation,'wall_seconds':measurement['wall_seconds']})
   (root/'runs/t9-campaign-index.json').write_text(json.dumps(manifest,indent=2)+'\n')
   print(project,scenario,sample,measurement['wall_seconds'],flush=True)
