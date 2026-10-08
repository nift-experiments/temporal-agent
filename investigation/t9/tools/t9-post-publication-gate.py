from pathlib import Path
import json,hashlib,subprocess
root=Path(__file__).resolve().parent.parent;results=[]
def manifest(base):return {str(p.relative_to(base)):hashlib.sha256(p.read_bytes()).hexdigest() for p in base.rglob('*') if p.is_file()}
for name in ['temporal','temporal-agent']:
 a=manifest(root/'repro'/name/'public');b=manifest(root.parent/name/'public');diff=[p for p in sorted(set(a)|set(b)) if a.get(p)!=b.get(p)];assert not diff,(name,diff)
 assert not subprocess.check_output(['git','status','--porcelain'],cwd=root.parent/name,text=True).strip()
 results.append({'project':name,'files':len(b),'final_publication_equals_accepted_clean_clone':True,'source_clean':True})
a=manifest(root/'reference/t1-complete-history');b=manifest(root/'build-work/build');diff=[p for p in sorted(set(a)|set(b)) if a.get(p)!=b.get(p)];assert set(diff)<=set(['.og-image-stats.json']),diff
results.append({'project':'upstream','files':len(b),'reference_identical_files':len(a)-len(diff),'operational_difference_only':diff})
(root/'runs/t9-post-publication-gate.json').write_text(json.dumps(results,indent=2)+'\n');print(results)
