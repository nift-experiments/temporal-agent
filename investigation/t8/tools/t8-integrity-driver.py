from pathlib import Path
import subprocess
root=Path(__file__).resolve().parent.parent
for script in ['region-input-equality.py','cache-input-integrity.py','t8-lifecycle-equality.py']:
 subprocess.run(['python3',str(root/'tools'/script)],check=True)
