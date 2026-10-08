from pathlib import Path
import subprocess,os,json
root=Path(__file__).resolve().parent.parent
node=root/'toolchain/node-v24.21.0-linux-x64/bin/node'
env={**os.environ,'PLAYWRIGHT_BROWSERS_PATH':str(root/'toolchain/playwright-browsers')}
def run(script,*args):
 cmd=['python3' if script.endswith('.py') else str(node),str(root/'tools'/script),*args]
 subprocess.run(cmd,env=env,check=True)
for script in ['t8-semantic-parity.cjs','t8-code-token-parity.cjs','t8-navbar-parity.cjs','t8-link-audit.cjs','t8-projections.py','t8-assets.py']:run(script)
for name,port in [('authored','4392'),('agent','4393')]:
 base='http://127.0.0.1:'+port
 for script,kind in [('browser-full-publication.cjs','full'),('browser-project-interactions.cjs','interactions'),('browser-special-interactions.cjs','special'),('browser-supplemental-interactions.cjs','supplemental')]:run(script,'t8-'+kind+'-'+name,base)
run('compare-t8-states.py','t8-full-authored','t8-full-agent')

for name,port in [('authored','4392'),('agent','4393')]:run('browser-visual-audit.cjs','t8-visual-'+name,'http://127.0.0.1:'+port)
run('compare-t8-visuals.cjs')

run('compare-t8-interactions.py')
