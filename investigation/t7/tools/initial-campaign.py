from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parent.parent
projects=['upstream','temporal','temporal-agent']
for sample in range(2,6):
 order=projects[(sample-2)%3:]+projects[:(sample-2)%3]
 for project in order:
  label=f't7-initial-{project}-warm-full-{sample}'
  command=[sys.executable,str(root/'tools/measure-publication.py'),'--project',project,'--label',label]+([] if project=='upstream' else ['--force'])
  with (root/'runs'/f'{label}-summary.log').open('wb') as log:subprocess.run(command,stdout=log,stderr=subprocess.STDOUT,check=True)
  print(label,'complete',flush=True)
