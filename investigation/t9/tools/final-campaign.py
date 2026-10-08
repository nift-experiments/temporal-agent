"""Serialized five-sample complete publication campaign; no dependency acquisition."""
from pathlib import Path
import subprocess,json,shutil,os,hashlib
root=Path(__file__).resolve().parent.parent
projects=['upstream','temporal','temporal-agent'];samples=5
manifest={'definitions':{'warm-full':'Complete upstream production command; Nift --force recomputes conversion, bundles, body/shell/projections, and all Nift pages. Installed dependencies and OS caches retained.','fresh-app':'Delete application/compiler/publication caches (upstream includes OG cache); preserve installed dependencies and pinned external source clone. Nift maintained OG assets remain source inputs, not caches. OS caches uncontrolled.','unchanged':'Normal complete command with unchanged maintained inputs after prior publication; upstream still runs prebuild/build/postbuild.'},'runs':[]}
for project in projects:
 cwd=root/'build-work' if project=='upstream' else root.parent/project
 manifest.setdefault('source_commits',{})[project]=subprocess.check_output(['git','rev-parse','HEAD'],cwd=cwd,text=True).strip()
 if project!='upstream':assert not subprocess.check_output(['git','status','--porcelain'],cwd=cwd,text=True).strip(), 'Final campaign requires clean maintained sources'
for scenario in ['warm-full','fresh-app','unchanged']:
 for sample in range(1,samples+1):
  offset=(sample-1)%3;order=projects[offset:]+projects[:offset]
  for project in order:
   preparation=[]
   if scenario=='fresh-app':
    cwd=root/'build-work' if project=='upstream' else root.parent/project
    directories=['.docusaurus','build','node_modules/.cache'] if project=='upstream' else ['.cache','public','.nift/public']
    for directory in directories:
     target=cwd/directory;shutil.rmtree(target,ignore_errors=True);preparation.append(str(target))
   label='t9-'+project+'-'+scenario+'-'+str(sample)
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
