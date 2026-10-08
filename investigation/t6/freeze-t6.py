from pathlib import Path
import json,shutil
base=Path(__file__).resolve().parent.parent;runs=base/'runs';visual=json.loads((runs/'t6-visual-comparison-v3.json').read_text());assert len(visual)==32 and all(r['geometryIdentical'] and r['maxChannelDifference']<=1 for r in visual);tokens=json.loads((runs/'t6-code-token-parity.json').read_text());assert len(tokens)==1924 and all(r['identical'] for r in tokens);links=json.loads((runs/'t6-whole-site-links.json').read_text());assert all(not r['missing'] for r in links['results'])
for name in ['temporal','temporal-agent']:
 root=base.parent/name;out=root/'investigation/t6';out.mkdir(parents=True,exist_ok=True)
 for p in runs.glob('t6-*'):
  if p.is_dir():shutil.copytree(p,out/p.name,dirs_exist_ok=True)
  else:shutil.copy2(p,out/p.name)
 for name2 in ['whole-site-link-audit.cjs','browser-visual-audit.cjs','compare-visuals.cjs','code-token-parity.cjs','freeze-t6.py']:shutil.copy2(base/'tools'/name2,out/name2)
 shutil.copy2(base/'source-audit/nift-binary-pin.json',out/'nift-binary-pin.json')
 (root/'investigation/T6-PARITY.md').write_text('''# T6 whole-site publication/browser parity accepted

Publication scope: 962 HTML routes, with 793 primary routes and 169 special routes. T5 body/metadata checks cover every route. All 832 Markdown/text/sitemap products and 1,130 maintained non-framework assets are byte-identical. All 4,544 code blocks per project match pinned token classes, styles and text. All HTML pages pass internal links and asset references: no missing paths in reference or migrations. Published framework bundles are replaced by migration island bundles; the upstream operational OG-statistics sidecar is not a publication product. No claim of identical total file count or complete JavaScript-byte equality is made.

Representative browser parity: 132 states per migration, zero recorded differences or page errors. Real interactions: 49 cases per migration against deterministic local transports. Portable gateways preserve 563 concrete redirect samples from 567 rules, Markdown content negotiation, trailing-slash redirects and HTML/Markdown 404 behavior. Hosted Vercel, live Algolia index quality, Kapa backend, feedback submission and telemetry backends are not exercised.

Visual review: eight representative families at desktop/mobile dark theme, 16 screenshots per implementation and 32 reference comparisons. All recorded geometry is identical. 21 comparisons are pixel-identical; 11 differ in 21 pixels by one channel level (maximum), retained as rasterization noise, not claimed pixel identity.

Rejected visual drafts found three actual migration omissions: cookbook/main-doc index ID collision in navigation, Home navbar incorrectly active despite pinned activeBasePath:none, and missing upstream Prism additional-language initialization. All fixed migration-side; draft images/results retained. The scoped main-doc sidebar now prevents cookbook index overwrites, while the agent project maintains its own corrected explicit navigation. Original Prism initialization is retained on server and client.

Nift core and templates are unchanged. The existing installed Nift v4.9.0 executable has been snapshotted and SHA-256 pinned before T7–T9 formal timings. Earlier timing logs are candidate diagnostics, not accepted benchmark results. Initial full publication, lifecycle correctness, profiling, optimization and final fresh-clone benchmark work remain T7–T9.
''')
 with (root/'investigation/KNOWN-DIVERGENCES.md').open('a') as f:f.write('\n| T6-VISUAL | Representative screenshots | Eleven final comparisons differ in 21 pixels by at most one channel level | rasterization noise | investigation/t6/t6-visual-comparison-v3.json | Geometry, token styles and recorded behavior identical; exact pixel identity not claimed | Classified; no functional/layout defect |\n| T6-NAV-PRISM | Navigation and code highlighting | Draft ID collision, active Home link and missing language initialization | resolved migration regressions | T6 rejected/final screenshot and token audits | Restored pinned group boundaries/config/initializer without core changes | Resolved |\n')
 with (root/'HANDOVER.md').open('a') as f:f.write('\n## T6 accepted\n\nWhole-site publication and representative browser parity accepted; all 4,544 highlighted code blocks verified per project. 32 visual comparisons have identical geometry and max channel delta 1 after resolving real draft defects. See investigation/T6-PARITY.md. Next T7: separately installed frozen dependencies, initial whole-pipeline measurements and comprehensive incremental/forced equality; T8 profiling/optimization; T9 final serialized campaign and fresh-clone review. No final benchmark claim yet.\n')
 with (root/'investigation/STATUS.md').open('a') as f:f.write('\nT6 accepted: whole-site static/link/token audits plus representative visual/browser parity. T7–T9 remain.\n')
print('T6 accepted evidence frozen in both repositories')
