"""One serialized complete production command; dependencies and monitor are outside measured process tree."""
from pathlib import Path
import argparse,datetime,json,os,resource,subprocess,time
root=Path(__file__).resolve().parent.parent
p=argparse.ArgumentParser();p.add_argument('--project',choices=['upstream','temporal','temporal-agent'],required=True);p.add_argument('--label',required=True);p.add_argument('--force',action='store_true');a=p.parse_args();out=root/'runs'/a.label
if out.exists():raise SystemExit('Refuse overwrite')
out.mkdir(parents=True);env=os.environ.copy();env['PATH']=str(root/'toolchain/frozen-bin')+os.pathsep+str(root/'toolchain/node-v24.21.0-linux-x64/bin')+os.pathsep+env['PATH']
if a.project=='upstream':cwd=root/'build-work';command=[str(root/'toolchain/yarn/node_modules/.bin/yarn'),'build']
else:cwd=root.parent/a.project;command=[str(root/'toolchain/node-v24.21.0-linux-x64/bin/node'),'tools/publish.cjs']+(['--force'] if a.force else [])
def tree(pid):
 values=[];pending=[pid];seen=set()
 while pending:
  current=pending.pop()
  if current in seen:continue
  seen.add(current)
  try:
   rss=int(Path(f'/proc/{current}/statm').read_text().split()[1])*os.sysconf('SC_PAGE_SIZE');values.append((current,rss))
   pending.extend(int(v) for v in Path(f'/proc/{current}/task/{current}/children').read_text().split())
  except (FileNotFoundError,ProcessLookupError,PermissionError):pass
 return values
start=time.perf_counter();samples=[]
with (out/'production.log').open('wb') as log:
 child=subprocess.Popen(command,cwd=cwd,env=env,stdout=log,stderr=subprocess.STDOUT)
 while child.poll() is None:
  processes=tree(child.pid);samples.append({'elapsed_seconds':time.perf_counter()-start,'rss_sum_mib':sum(r for _,r in processes)/1048576,'processes':len(processes)});time.sleep(.05)
 code=child.wait()
wall=time.perf_counter()-start;record={'project':a.project,'command':command,'timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':code,'wall_seconds':wall,'maximum_individual_descendant_rss_mib':resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss/1024,'sampled_descendant_rss_sum_peak_mib':max((r['rss_sum_mib'] for r in samples),default=0),'sample_period_target_seconds':.05,'rss_qualification':'ru_maxrss is maximum individual descendant process/phase; sampled sum is aggregate resident-page counts, includes shared-page double counting, is not PSS and may miss peaks','dependency_acquisition_outside_timing':True,'os_caches':'uncontrolled','production_not_dev_hmr':True,'force':a.force}
if a.project!='upstream':record['components']=json.loads((cwd/'.cache/publication-metrics.json').read_text())
else:
 clone=Path('/tmp/ai-cookbook-sync/repo');pin=subprocess.check_output(['git','rev-parse','HEAD'],cwd=clone,text=True).strip();record['cookbook_pin']=pin
 if pin!='2385cc030f9ca1cc67b05082f1990d20cfc3a38c':record['invalid_reason']='Cookbook source pin changed'
 text=(out/'production.log').read_text(errors='replace')
 if 'Creating placeholder directory' in text or 'created placeholder' in text:record['invalid_reason']='Offline placeholder fallback'
(out/'measurement.json').write_text(json.dumps(record,indent=2)+'\n');(out/'sampled-tree-rss.json').write_text(json.dumps(samples,indent=2)+'\n');print(json.dumps(record,indent=2),flush=True)
if code or record.get('invalid_reason'):raise SystemExit(code or 1)
