from pathlib import Path
import json,re
root=Path(__file__).resolve().parent.parent
results=[]
def normalize(value):return re.sub(r'http://127\.0\.0\.1:\d+','LOCAL_ORIGIN',json.dumps(value,sort_keys=True))
for project in ['authored','agent']:
 for kind,reference in [('interactions','t3-reference-interactions-v7'),('special','t5-special-reference-v2'),('supplemental','t5-supplemental-reference-v2')]:
  ref=json.loads((root/'runs'/reference/'observations.json').read_text());data=json.loads((root/'runs'/('t8-'+kind+'-'+project)/'observations.json').read_text());assert not data['errors'];assert len(ref['cases'])==len(data['cases'])
  for a,b in zip(ref['cases'],data['cases']):results.append({'project':project,'family':kind,'case':a['name'],'identical':normalize(a)==normalize(b)})
(root/'runs/t8-interaction-comparison.json').write_text(json.dumps(results,indent=2)+'\n')
print('Interaction comparisons',len(results),'differences',[r for r in results if not r['identical']]);assert all(r['identical'] for r in results)
