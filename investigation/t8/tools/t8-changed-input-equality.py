"""Changed-input complete production checks, with restored maintained sources."""
import pathlib,subprocess,json,hashlib,os,time,re,sys
root=pathlib.Path(__file__).resolve().parent.parent;node=root/'toolchain/node-v24.21.0-linux-x64/bin/node';env={**os.environ,'PATH':str(root/'toolchain/frozen-bin')+':'+os.environ['PATH']};records=[]
def manifest(repo):return {str(p.relative_to(repo/'public')):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((repo/'public').rglob('*')) if p.is_file()}
def execute(repo,args,log):
 with log.open('w') as f:subprocess.run([str(node),*args],cwd=repo,env=env,stdout=f,stderr=subprocess.STDOUT,check=True)
for name in (sys.argv[1:] or ['temporal','temporal-agent']):
 repo=root.parent/name;agent=name.endswith('-agent');rows=json.loads((repo/'models/routes.json').read_text());primary=[r for r in rows if r.get('source') and r['source'].startswith('docs/')] if not agent else [r for r in rows if r.get('body','').startswith('html/') and not r.get('kind') and not r['body'].startswith('html/special/') and r['route']!='/']
 cli=next(r for r in rows if r['route']=='/cli/setup-cli');retry=next(r for r in rows if r['route']=='/encyclopedia/retry-policies')
 for case in ['body-1','body-10','body-100','metadata','shared-layout','navigation','diagram','generated-synced','search-visible','island-source']:
  out=root/'runs'/('t8-change-'+name+'-'+case);out.mkdir(exist_ok=False);saved={};assets=set((repo/'static/img/og').glob('*.jpg'));maintenance=0
  marker='TEMPORAL_T8_'+case.upper().replace('-','_')
  def save(p):
   if p not in saved:saved[p]=p.read_bytes()
   return p
  def update_full(row,addition):
   p=save(repo/'downloads/llms-full.txt');text=p.read_text();url='https://docs.temporal.io'+row['route'].rstrip('/');match=re.search(r'^Source: '+re.escape(url)+r'/?$',text,re.M)
   if match:
    end=text.find('\n---\n',match.end());end=len(text) if end<0 else end;text=text[:end]+'\n\n'+addition+'\n'+text[end:];p.write_text(text)
  def append(row):
   if agent:
    relative=('index' if row['route']=='/' else row['route'].strip('/'))+'.md';download=repo/'downloads'/relative
    if download.exists():p=save(download);p.write_text(p.read_text()+'\n'+marker+'\n')
    update_full(row,marker)
   p=save(repo/(row['body'] if agent else row['source']));p.write_bytes(p.read_bytes()+(('\n<p>'+marker+'</p>\n') if agent else ('\n\n```text\n'+marker+'\n```\n')).encode())
  try:
   if case.startswith('body-'):
    for row in primary[:int(case.split('-')[1])]:append(row)
   elif case=='metadata':
    save(repo/'models/og-images.json')
    if agent:
     p=save(repo/'models/routes.json');data=json.loads(p.read_text());x=next(r for r in data if r['key']==cli['key']);x['metadata']['title']+=' '+marker;x['metadata']['description']+=' '+marker;p.write_text(json.dumps(data,indent=2)+'\n')
     html=save(repo/cli['body']);html.write_text(html.read_text().replace(cli['metadata']['title'],x['metadata']['title']))
     md=save(repo/'downloads/cli/setup-cli.md');md.write_text(md.read_text().replace('# '+cli['metadata']['title'],'# '+x['metadata']['title'],1).replace('> '+cli['metadata']['description'],'> '+x['metadata']['description'],1))
     for index in (repo/'downloads').rglob('*.txt'):
      text=index.read_text();old_link='['+cli['metadata']['title']+'](https://docs.temporal.io/cli/setup-cli.md)';new_link='['+x['metadata']['title']+'](https://docs.temporal.io/cli/setup-cli.md)';changed=text.replace(old_link,new_link)
      if index.name=='llms-full.txt':changed=changed.replace('# '+cli['metadata']['title']+'\n\nSource: https://docs.temporal.io/cli/setup-cli','# '+x['metadata']['title']+'\n\nSource: https://docs.temporal.io/cli/setup-cli',1)
      if changed!=text:save(index);index.write_text(changed)
    else:
     p=save(repo/cli['source']);s=p.read_text();s=s.replace('title: Install and configure the CLI','title: Install and configure the CLI '+marker).replace('description: Install the Temporal CLI, run a local development server, and configure your environment.','description: Install the Temporal CLI, run a local development server, and configure your environment. '+marker);p.write_text(s)
    t=time.monotonic();execute(repo,['tools/refresh-og.cjs','--route',cli['route']],out/'selective-og-maintenance.log');maintenance=time.monotonic()-t
   elif case=='shared-layout':
    p=save(repo/'models/chrome/footer.html');p.write_bytes(p.read_bytes().replace(b'</footer>',('<span>'+marker+'</span></footer>').encode()))
   elif case=='navigation':
    p=save(repo/('models/navigation.json' if agent else 'sidebars.js'))
    if agent:
     data=json.loads(p.read_text())
     def change(items):
      for x in items:
       if x.get('label')=='Temporal Cloud':x['label']+=' '+marker;return True
       if change(x.get('items',[])):return True
      return False
     assert change(data['documentation']);p.write_text(json.dumps(data,indent=2)+'\n')
    else:
     old=p.read_text();new=old.replace('label: "Temporal Cloud"','label: "Temporal Cloud '+marker+'"').replace("label: 'Temporal Cloud'","label: 'Temporal Cloud "+marker+"'");assert new!=old;p.write_text(new)
   elif case=='diagram':
    row=next(r for r in rows if (r.get('source')=='docs/cloud/connectivity/aws-connectivity.mdx') or (agent and r['route']=='/cloud/connectivity/aws-connectivity'))
    p=save(repo/(row['body'] if agent else row['source']));old=p.read_text();new=old.replace('flowchart LR','flowchart TB').replace('graph LR','graph TB').replace('graph TD','graph LR');assert new!=old;p.write_text(new)
   elif case=='generated-synced':
    if agent:
     row=next(r for r in rows if r['route']=='/ai/cookbook/basic-openai-python');append(row)
    else:
     p=save(repo/'references/cookbook-source/deep_research/basic_openai_python/README.md');p.write_text(p.read_text()+'\n\n```text\n'+marker+'\n```\n')
     # Generated outputs are owned by the local converter; restore them too.
     for p in (repo/'ai-cookbook').rglob('*'):
      if p.is_file():save(p)
   elif case=='search-visible':
    append(cli)
   elif case=='island-source':
    p=save(repo/('islands-src' if agent else 'src')/'components/Demos/RetrySimulator/RetrySimulator.js');old=p.read_text();new=old.replace('<h3>Sample Activity</h3>','<h3>Sample Activity '+marker+'</h3>');assert old!=new;p.write_text(new)
    if agent:
     for row in rows:
      p=repo/row['body']
      if 'data-temporal-island="Retry"' in p.read_text():save(p)
     t=time.monotonic();execute(repo,['tools/refresh-islands.cjs','--island','Retry'],out/'selective-island-maintenance.log');maintenance=time.monotonic()-t
   t=time.monotonic();execute(repo,['tools/publish.cjs'],out/'incremental.log');elapsed=time.monotonic()-t;components=json.loads((repo/'.cache/publication-metrics.json').read_text());inc=manifest(repo)
   # Verify the change reached publication, not merely that two no-op builds agree.
   if case!='diagram':assert any(marker.encode() in p.read_bytes() for p in (repo/'public').rglob('*.html'))
   execute(repo,['tools/publish.cjs','--force'],out/'forced.log');clean=manifest(repo);diff=[p for p in sorted(set(inc)|set(clean)) if inc.get(p)!=clean.get(p)]
   result={'project':name,'case':case,'incremental_seconds':elapsed,'explicit_maintenance_seconds':maintenance,'whole_operation_seconds':elapsed+maintenance,'files':len(clean),'independent_clean_forced_equal':not diff,'differences':diff,'observable_change_verified':True,'components':components};records.append(result);(out/'result.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
   if diff:raise RuntimeError('Incremental publication mismatch')
  finally:
   for p,data in saved.items():p.write_bytes(data)
   for p in set((repo/'static/img/og').glob('*.jpg'))-assets:p.unlink()
   execute(repo,['tools/publish.cjs'],out/'restore.log')
(root/'runs/t8-changed-input-equality.json').write_text(json.dumps(records,indent=2)+'\n')
