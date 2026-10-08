import pathlib,subprocess,json,hashlib
root=pathlib.Path(__file__).resolve().parent.parent;node=root/'toolchain/node-v24.21.0-linux-x64/bin/node';record=[]
def manifest(repo):return {str(p.relative_to(repo/'public')):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((repo/'public').rglob('*')) if p.is_file()}
for name in ['temporal','temporal-agent']:
 repo=root.parent/name;agent=name.endswith('-agent')
 for case,file in [('shared-footer',repo/'models/chrome/footer.html'),('navigation',repo/('models/navigation.json' if agent else 'sidebars.js'))]:
  original=file.read_bytes();marker=' TEMPORAL_T4_SHARED_PROOF'
  if case=='shared-footer':changed=original.replace(b'</footer>',b'<span>TEMPORAL_T4_SHARED_PROOF</span></footer>')
  elif agent:
   data=json.loads(original)
   def edit(items):
    for item in items:
     if item.get('label')=='Temporal Cloud':item['label']+=marker;return True
     if edit(item.get('items',[])):return True
    return False
   assert edit(data['documentation']);changed=(json.dumps(data,indent=2)+'\n').encode()
  else:
   changed=original.replace(b'label: "Temporal Cloud"',b'label: "Temporal Cloud'+marker.encode()+b'"').replace(b"label: 'Temporal Cloud'",b"label: 'Temporal Cloud"+marker.encode()+b"'")
  assert changed!=original
  out=root/'runs'/('t4-equality-'+name+'-'+case);out.mkdir(exist_ok=False)
  try:
   file.write_bytes(changed)
   with (out/'incremental.log').open('w') as log:subprocess.run([str(node),'tools/publish.cjs'],cwd=repo,stdout=log,stderr=subprocess.STDOUT,check=True)
   incremental=manifest(repo)
   with (out/'forced.log').open('w') as log:subprocess.run([str(node),'tools/publish.cjs','--force'],cwd=repo,stdout=log,stderr=subprocess.STDOUT,check=True)
   forced=manifest(repo);diff=[p for p in set(incremental)|set(forced) if incremental.get(p)!=forced.get(p)];result={'project':name,'case':case,'incremental_equals_clean_forced':not diff,'files':len(forced),'differences':diff};record.append(result);(out/'result.json').write_text(json.dumps(result,indent=2)+'\n');print(result,flush=True)
   if diff:raise RuntimeError('Publication difference')
  finally:
   file.write_bytes(original)
   with (out/'restore.log').open('w') as log:subprocess.run([str(node),'tools/publish.cjs','--force'],cwd=repo,stdout=log,stderr=subprocess.STDOUT,check=True)
(root/'runs/t4-shared-equality.json').write_text(json.dumps(record,indent=2)+'\n')
