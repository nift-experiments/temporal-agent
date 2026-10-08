from pathlib import Path
import json
root=Path(__file__).resolve().parent.parent
checks=['t8-restored-semantic-parity.json','t8-post-matrix-code-token-parity.json','t8-navbar-parity.json','t8-complete-projections.json','t8-maintained-assets.json','t8-restored-state-comparison.json','t8-interaction-comparison.json']
for name in checks:
 p=root/'runs'/name;data=json.loads(p.read_text());assert all(r['identical'] for r in data),name
visual=json.loads((root/'runs/t8-visual-comparison.json').read_text());assert len(visual)==32 and all(r['geometryIdentical'] and r['maxChannelDifference']<=1 for r in visual)
for name in ['authored','agent']:
 for kind in ['full','interactions','special','supplemental','visual']:
  data=json.loads((root/'runs'/('t8-'+kind+'-'+name)/'observations.json').read_text());assert not data['errors']
print('T8 restored whole-site/browser/visual acceptance checks passed')
