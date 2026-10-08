"""Real authored/rendered publication lifecycle; clean recomputation is independent."""
import pathlib,subprocess,json,hashlib,os,time,sys
root=pathlib.Path(__file__).resolve().parent.parent
node=root/'toolchain/node-v24.21.0-linux-x64/bin/node'
env={**os.environ,'PATH':str(root/'toolchain/frozen-bin')+':'+os.environ['PATH']}
record=[]
def manifest(repo):
 return {str(p.relative_to(repo/'public')):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((repo/'public').rglob('*')) if p.is_file()}
def execute(repo,args,log):
 with log.open('w') as f:subprocess.run([str(node),*args],cwd=repo,env=env,stdout=f,stderr=subprocess.STDOUT,check=True)
def compare(repo,name,case,expect):
 out=root/'runs'/('t9-lifecycle-'+name+'-'+case);out.mkdir(exist_ok=False)
 label='t9-measured-change-'+name+'-'+case
 subprocess.run(['python3',str(root/'tools/measure-publication.py'),'--project',name,'--label',label],env=env,check=True,stdout=(out/'measurement-output.log').open('w'));measurement=json.loads((root/'runs'/label/'measurement.json').read_text());elapsed=measurement['wall_seconds']
 expect(repo);inc=manifest(repo)
 execute(repo,['tools/publish.cjs','--force'],out/'forced.log');clean=manifest(repo)
 diff=[p for p in sorted(set(inc)|set(clean)) if inc.get(p)!=clean.get(p)]
 r={'project':name,'case':case,'incremental_seconds':elapsed,'files':len(clean),'independent_clean_forced_equal':not diff,'differences':diff,'expected_behavior_verified':True,'measurement':measurement};record.append(r);(out/'result.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r),flush=True)
 if diff:raise RuntimeError('Incremental publication differs from clean recomputation')
for name in (sys.argv[1:] or ['temporal','temporal-agent']):
 repo=root.parent/name;agent=name.endswith('-agent');registry=repo/'models/routes.json';og=repo/'models/og-images.json'
 saved={p:p.read_bytes() for p in [registry,og,*([repo/'downloads/llms.txt',repo/'downloads/llms-full.txt'] if agent else [])]};original_assets=set((repo/'static/img/og').glob('*.jpg'))
 source=repo/('html/t7-lifecycle.html' if agent else 'docs/t7-lifecycle.mdx');download=repo/'downloads/t7-lifecycle.md';renamed=repo/'downloads/t7-lifecycle-renamed.md'
 row=None
 try:
  if agent:
   rows=json.loads(registry.read_text());template=next(r for r in rows if r.get('body') and r['route']=='/cloud/get-started/users-invite')
   row=json.loads(json.dumps(template));row.update(key='t7-lifecycle',route='/t7-lifecycle',body='html/t7-lifecycle.html',shellKey=template['key']);row['metadata'].update(id='t7-lifecycle',title='T7 lifecycle fixture',description='A bounded publication lifecycle fixture.',permalink='/t7-lifecycle',tags=[],toc=[],breadcrumbLabel='T7 lifecycle fixture');row['metadata'].pop('previous',None);row['metadata'].pop('next',None)
   source.write_text('<article class="theme-doc-markdown markdown"><h1>T7 lifecycle fixture</h1><p>T7_LIFECYCLE_BODY</p></article>');rows.append(row);registry.write_text(json.dumps(rows,indent=2)+'\n');download.write_text('# T7 lifecycle fixture\n\nT7_LIFECYCLE_BODY\n');index=repo/'downloads/llms.txt';index.write_text(index.read_text()+'\n## Lifecycle fixture\n\n- [T7 lifecycle fixture](https://docs.temporal.io/t7-lifecycle.md): A bounded publication lifecycle fixture.\n');full=repo/'downloads/llms-full.txt';full.write_text(full.read_text()+'\n---\n\n# T7 lifecycle fixture\n\nSource: https://docs.temporal.io/t7-lifecycle\n\nT7_LIFECYCLE_BODY\n')
  else:source.write_text('---\ntitle: T7 lifecycle fixture\ndescription: A bounded publication lifecycle fixture.\nslug: /t7-lifecycle\ntags: [t7-lifecycle-tag]\n---\n\n# T7 lifecycle fixture\n\nT7_LIFECYCLE_BODY\n')
  out=root/'runs'/('t9-lifecycle-'+name+'-maintenance');out.mkdir(exist_ok=False)
  execute(repo,['tools/refresh-og.cjs','--route','/t7-lifecycle'],out/'og-add.log')
  def added(r):
   assert (r/'public/t7-lifecycle/index.html').is_file();assert (r/'public/t7-lifecycle.md').is_file();assert 'T7_LIFECYCLE_BODY' in (r/'public/t7-lifecycle/index.html').read_text();assert 'https://docs.temporal.io/t7-lifecycle' in (r/'public/sitemap.xml').read_text();assert 'Source: https://docs.temporal.io/t7-lifecycle' in (r/'public/llms-full.txt').read_text()
   if not agent:assert (r/'public/tags/t-7-lifecycle-tag/index.html').is_file()
  compare(repo,name,'route-add',added)
  if agent:
   rows=json.loads(registry.read_text());row=next(r for r in rows if r['key']=='t7-lifecycle');row['route']='/t7-lifecycle-renamed';row['metadata']['permalink']=row['route'];registry.write_text(json.dumps(rows,indent=2)+'\n');download.rename(renamed)
   for projection in [repo/'downloads/llms.txt',repo/'downloads/llms-full.txt']:projection.write_text(projection.read_text().replace('https://docs.temporal.io/t7-lifecycle','https://docs.temporal.io/t7-lifecycle-renamed'))
  else:source.write_text(source.read_text().replace('slug: /t7-lifecycle\n','slug: /t7-lifecycle-renamed\n'))
  def moved(r):
   assert not (r/'public/t7-lifecycle/index.html').exists();assert not (r/'public/t7-lifecycle.md').exists();assert (r/'public/t7-lifecycle-renamed/index.html').is_file();assert (r/'public/t7-lifecycle-renamed.md').is_file();assert 'Source: https://docs.temporal.io/t7-lifecycle-renamed' in (r/'public/llms-full.txt').read_text();assert 'Source: https://docs.temporal.io/t7-lifecycle\n' not in (r/'public/llms-full.txt').read_text();assert 'https://docs.temporal.io/t7-lifecycle-renamed' in (r/'public/t7-lifecycle-renamed/index.html').read_text()
  compare(repo,name,'route-rename',moved)
  if agent:
   rows=json.loads(registry.read_text());registry.write_text(json.dumps([r for r in rows if r['key']!='t7-lifecycle'],indent=2)+'\n');renamed.unlink()
   for projection in [repo/'downloads/llms.txt',repo/'downloads/llms-full.txt']:projection.write_bytes(saved[projection])
  source.unlink()
  def removed(r):
   assert not (r/'public/t7-lifecycle-renamed/index.html').exists();assert not (r/'public/t7-lifecycle-renamed.md').exists();assert 'https://docs.temporal.io/t7-lifecycle-renamed' not in (r/'public/sitemap.xml').read_text();assert 'Source: https://docs.temporal.io/t7-lifecycle-renamed' not in (r/'public/llms-full.txt').read_text()
   if not agent:assert not (r/'public/tags/t-7-lifecycle-tag/index.html').exists()
  compare(repo,name,'route-delete',removed)
 finally:
  for p,data in saved.items():p.write_bytes(data)
  for p in [source,download,renamed]:p.unlink(missing_ok=True)
  for p in set((repo/'static/img/og').glob('*.jpg'))-original_assets:p.unlink()
  restore=root/'runs'/('t9-lifecycle-'+name+'-restore.log');execute(repo,['tools/publish.cjs'],restore)
(root/'runs/t9-lifecycle-equality.json').write_text(json.dumps(record,indent=2)+'\n')
