#help

import subprocess
import sys

def pwshell():
    p = subprocess.Popen(["powershell.exe", 
                ".\\getservices.ps1"], 
                stdout=sys.stdout)
    p.communicate()
