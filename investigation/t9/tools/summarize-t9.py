from pathlib import Path
import json,statistics,hashlib
root=Path(__file__).resolve().parent.parent
index=json.loads((root/'runs/t9-campaign-index.json').read_text());assert len(index['runs'])==45
summary={'definitions':index['definitions'],'source_commits':index['source_commits'],'scenarios':{},'components':{},'changes':json.loads((root/'runs/t9-changed-input-equality.json').read_text()),'lifecycle':json.loads((root/'runs/t9-lifecycle-equality.json').read_text()),'fresh_clones':json.loads((root/'runs/t9-clean-clones/result.json').read_text()),'upstream_changes':json.loads((root/'runs/t9-upstream-changed-inputs.json').read_text()),'post_publication_gate':json.loads((root/'runs/t9-post-publication-gate.json').read_text())}
for scenario in ['warm-full','fresh-app','unchanged']:
 summary['scenarios'][scenario]={}
 for project in ['upstream','temporal','temporal-agent']:
  data=[json.loads((root/'runs'/r['label']/'measurement.json').read_text()) for r in index['runs'] if r['scenario']==scenario and r['project']==project];assert len(data)==5 and all(x['exit_code']==0 and not x.get('invalid_reason') for x in data)
  result={'samples':5}
  for key in ['wall_seconds','maximum_individual_descendant_rss_mib','sampled_descendant_rss_sum_peak_mib']:
   values=[x[key] for x in data];result[key]={'median':statistics.median(values),'range':[min(values),max(values)]}
  result['output_counts']=sorted(set(x['components']['files'] for x in data if 'components' in x));result['output_bytes']=sorted(set(x['components']['bytes'] for x in data if 'components' in x))
  if project=='upstream':
   result['og_stats']=[x.get('og_stats') for x in data]
   assert all(x.get('og_stats') and x['og_stats']['generated']==(792 if scenario=='fresh-app' else 0) for x in data), 'OG cache boundary mismatch'
   result['output_counts']=sorted(set(x['output']['files'] for x in data));result['output_bytes']=sorted(set(x['output']['bytes'] for x in data))
   phase_keys=set.intersection(*(set(x.get('observed_phase_seconds',{})) for x in data));summary['components'][scenario+'-upstream']={k:{'median':statistics.median(max(0,x['observed_phase_seconds'][k]) for x in data),'range':[min(max(0,x['observed_phase_seconds'][k]) for x in data),max(max(0,x['observed_phase_seconds'][k]) for x in data)]} for k in sorted(phase_keys)}
  summary['scenarios'][scenario][project]=result
  if project!='upstream':
   keys=set.intersection(*(set(x['components']['stages']) for x in data));summary['components'][scenario+'-'+project]={k:{'median':statistics.median(x['components']['stages'][k] for x in data),'range':[min(x['components']['stages'][k] for x in data),max(x['components']['stages'][k] for x in data)]} for k in sorted(keys)}
assert len(summary['changes'])==20 and len(summary['lifecycle'])==6 and all(r['independent_clean_forced_equal'] for r in summary['changes']+summary['lifecycle'])
assert all(r['byte_manifest_equals_working_publication'] and r['source_clean'] for r in summary['fresh_clones'])
(root/'runs/t9-final-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary['scenarios'],indent=2))
