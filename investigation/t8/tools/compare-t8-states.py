import pathlib,json,sys
root=pathlib.Path(__file__).resolve().parent.parent
ref=json.loads((root/'runs/t5-full-reference-v2/observations.json').read_text())
key=lambda r:(r['viewport'],r['requestedTheme'],r['route'])
refs={key(r):r for r in ref['states']};results=[]
for label in sys.argv[1:]:
 data=json.loads((root/'runs'/label/'observations.json').read_text())
 for r in data['states']:
  a=refs[key(r)];diff={k:{'reference':a.get(k),'migration':v} for k,v in r.items() if a.get(k)!=v}
  results.append({'label':label,'state':key(r),'identical':not diff,'differences':diff})
 print(label,len(data['states']),'differences',sum(bool(r['differences']) for r in results if r['label']==label),'errors',len(data['errors']))
(root/'runs/t8-restored-state-comparison.json').write_text(json.dumps(results,indent=2)+'\n')

assert all(r['identical'] for r in results)
