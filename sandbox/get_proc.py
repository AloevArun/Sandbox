import subprocess
cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Description,Id'
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
for line in proc.stdout:
    if not line.decode('cp866')[0].isspace():
        print(line.decode('cp866').rstrip())
