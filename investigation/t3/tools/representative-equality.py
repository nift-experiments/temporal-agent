import pathlib,subprocess,json,hashlib,time,sys
label=sys.argv[1] if len(sys.argv)>1 else "t3"
root=pathlib.Path(__file__).resolve().parent.parent;node=root/'toolchain/node-v24.21.0-linux-x64/bin/node'
def manifest(repo):return {str(p.relative_to(repo/'public')):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((repo/'public').rglob('*')) if p.is_file()}
record=[]
for name in ['temporal','temporal-agent']:
 repo=root.parent/name;agent=name.endswith('-agent')
 cases=[('body',repo/('html/cli/setup-cli.html' if agent else 'docs/cli/setup-cli.mdx'))]
 if not agent:cases.append(('include',repo/'docs/cloud/references/regions/awsregions.md'))
 cases.append(('route-shell',repo/'models/shells/cli.html'))
 for case,file in cases:
  original=file.read_bytes();marker='TEMPORAL_T3_EQUALITY_@content_$[rawHtml("literal")]'
  if case=='route-shell':changed=original.replace(b'</footer>',b'<span>'+marker.encode()+b'</span></footer>')
  elif agent:changed=original+b'<p>'+marker.encode()+b'</p>'
  else:changed=original+b'\n\n```text\n'+marker.encode()+b'\n```\n'
  assert changed!=original
  output=root/'runs'/(label+'-equality-'+name+'-'+case);output.mkdir(exist_ok=False)
  try:
   file.write_bytes(changed)
   with (output/'incremental.log').open('w') as log:subprocess.run([str(node),'tools/publish.cjs'],cwd=repo,stdout=log,stderr=subprocess.STDOUT,check=True)
   incremental=manifest(repo)
   with (output/'forced.log').open('w') as log:subprocess.run([str(node),'tools/publish.cjs','--force'],cwd=repo,stdout=log,stderr=subprocess.STDOUT,check=True)
   forced=manifest(repo);difference=[p for p in set(incremental)|set(forced) if incremental.get(p)!=forced.get(p)]
   result={'project':name,'case':case,'incremental_equals_clean_public_forced':not difference,'files':len(forced),'differences':difference};record.append(result)
   (output/'result.json').write_text(json.dumps(result,indent=2)+'\n');print(result,flush=True)
   if difference:raise RuntimeError('Incremental/forced difference')
  finally:
   file.write_bytes(original)
   with (output/'restore.log').open('w') as log:subprocess.run([str(node),'tools/publish.cjs','--force'],cwd=repo,stdout=log,stderr=subprocess.STDOUT,check=True)
(root/('runs/'+label+'-representative-equality.json')).write_text(json.dumps(record,indent=2)+'\n')
