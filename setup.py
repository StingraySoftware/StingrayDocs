import subprocess
import os

subprocess.check_call(
    ["python", "setup.py", "install"],
    cwd=os.path.join(os.getcwd(), "stingray")
)
