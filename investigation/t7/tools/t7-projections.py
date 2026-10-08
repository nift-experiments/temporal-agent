from pathlib import Path
import hashlib,json
base=Path('/home/nick/Repositories/nift/nift-experiments');ref=base/'temporal-baseline/reference/t1-complete-history';files=[p for p in ref.rglob('*') if p.is_file() and (p.suffix in ['.md','.txt'] or p.name=='sitemap.xml')];results=[]
for name in ['temporal','temporal-agent']:
 for p in files:
  rel=p.relative_to(ref);q=base/name/'public'/rel;results.append({'project':name,'file':str(rel),'identical':q.exists() and q.read_bytes()==p.read_bytes()})
 print(name,len(files),'products',sum(not r['identical'] for r in results if r['project']==name),'differences')
(base/'temporal-baseline/runs/t7-complete-projections.json').write_text(json.dumps(results,indent=2)+'\n')
assert all(r['identical'] for r in results)
