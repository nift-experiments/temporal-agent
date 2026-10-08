from pathlib import Path
import json,hashlib
b=Path('/home/nick/Repositories/nift/nift-experiments');ref=b/'temporal-baseline/reference/t1-complete-history';results=[]
for name in ['temporal','temporal-agent']:
 for p in ref.rglob('*'):
  if not p.is_file():continue
  rel=p.relative_to(ref)
  if p.suffix in ['.html','.md','.txt','.xml'] or str(rel).startswith('assets/js/') or p.name=='.og-image-stats.json':continue
  q=b/name/'public'/rel
  results.append({'project':name,'asset':str(rel),'identical':q.exists() and q.read_bytes()==p.read_bytes()})
 print(name,'assets',sum(r['project']==name for r in results),'differences',[r['asset'] for r in results if r['project']==name and not r['identical']][:20])
(b/'temporal-baseline/runs/t7-maintained-assets.json').write_text(json.dumps(results,indent=2)+'\n')
assert all(r['identical'] for r in results)
