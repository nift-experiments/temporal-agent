from pathlib import Path
import json,shutil,re
base=Path(__file__).resolve().parent.parent;runs=base/'runs'
ref=json.loads((runs/'t5-supplemental-reference-v2/observations.json').read_text())
normalize=lambda cases:re.sub(r'http://127\.0\.0\.1:439[0-5]','LOCAL_ORIGIN',json.dumps(cases,sort_keys=True))
for label in ['t5-supplemental-authored-v3','t5-supplemental-agent-v3']:
 d=json.loads((runs/label/'observations.json').read_text());assert len(d['cases'])==10 and not d['errors'];assert normalize(d['cases'])==normalize(ref['cases'])
for label in ['t5-full-authored-v2','t5-full-agent-v2']:
 d=json.loads((runs/label/'observations.json').read_text());assert len(d['states'])==132 and not d['errors']
checks=json.loads((runs/'t5-full-state-comparison.json').read_text());assert len(checks)==264 and all(r['identical'] for r in checks)
for stem,count,reference in [('interactions',31,'t3-reference-interactions-v7'),('special',8,'t5-special-reference-v2')]:
 expected=json.loads((runs/reference/'observations.json').read_text())['cases']
 for kind in ['authored','agent']:
  data=json.loads((runs/('t5-'+stem+'-'+kind+'-v1')/'observations.json').read_text());assert len(data['cases'])==count and not data['errors'];assert normalize(data['cases'])==normalize(expected)
for name in ['temporal','temporal-agent']:
 root=base.parent/name;out=root/'investigation/t5';out.mkdir(parents=True,exist_ok=True)
 for p in runs.glob('t5-*'):
  if p.is_dir():shutil.copytree(p,out/p.name,dirs_exist_ok=True)
  elif p.is_file():shutil.copy2(p,out/p.name)
 for name2 in ['browser-full-publication.cjs','compare-full-states.py','browser-special-interactions.cjs','browser-supplemental-interactions.cjs','full-semantic-parity.cjs','deployment-project-audit.cjs','freeze-t5.py']:shutil.copy2(base/'tools'/name2,out/name2)
 p=root/'investigation/KNOWN-DIVERGENCES.md';s=p.read_text();s=s.replace('| T3-DETAILS | Cloud SLO details | Native open/close without upstream height animation; content, open state, keyboard/native summary and styling retained | implementation difference | representative open/close fixture | Lightweight controller follows authorized static/vanilla-first architecture; reduced-motion fixture matches observable state | Verified |','| T3-DETAILS | Cloud SLO details | T3 native controller lacked upstream height animation | resolved migration difference | T5 established interaction matrices, 31 cases per project | T5 now retains the original animated Details component with static rich HTML children | Resolved; original component retained |');p.write_text(s)
 p=root/'investigation/T5-SPECIAL-PUBLICATION.md';s=p.read_text().replace('# T5 special-publication candidate (not yet accepted)','# T5 special publication accepted').replace('These are publication checks, not final benchmark results.','These are publication checks, not final benchmark results. Both full browser matrices pass all 132 states with zero recorded differences and zero page errors. Established interactions (31), Event History interactions (8), and supplemental search/filter/priority interactions (10) pass per project. Supplemental comparisons normalize only the deterministic local origin ports.');s=s.replace('Fixes are undergoing revalidation. No T5 acceptance, T6 whole-site parity, or final timing claim is made yet.','These defects are fixed and revalidated. Search query/persisted-filter state uses explicit client mounting rather than hydrating against request-independent static state. All rejected audit drafts remain in the evidence. T5 is accepted; T6 whole-site parity and final timings are not claimed yet.');p.write_text(s)
 with (root/'HANDOVER.md').open('a') as f:f.write('\n## T5 accepted\n\nAll 962 HTML routes, 832 Markdown/text/sitemap products, and 1,130 retained non-framework assets verified against the pinned reference. Full representative browser parity: 132 states per project, zero differences/errors; 49 interaction cases per project. Portable redirect/Markdown/404 checks passed. See investigation/T5-SPECIAL-PUBLICATION.md and investigation/t5. Next: T6 whole-site parity, then T7 initial benchmarks and incremental correctness. No formal benchmark accepted yet.\n')
 with (root/'investigation/STATUS.md').open('a') as f:f.write('\nT5 accepted: generated cookbook ownership, special publication, retained islands and portable deployment checked. T6–T9 remain.\n')
print('T5 accepted evidence frozen in both repositories')
