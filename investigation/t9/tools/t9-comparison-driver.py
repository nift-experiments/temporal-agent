from pathlib import Path
import subprocess
root=Path(__file__).resolve().parent.parent
for script in ['t9-changed-input-equality.py','t9-lifecycle-equality.py','t9-upstream-changes.py','t9-post-publication-gate.py','summarize-t9.py','write-t9-report.py']:
 subprocess.run(['python3',str(root/'tools'/script)],check=True)
