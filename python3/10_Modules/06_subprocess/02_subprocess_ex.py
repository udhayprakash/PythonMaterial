import subprocess
import sys

if sys.platform == "win32":
    subprocess.call(["dir", "/x"], shell=False)
else:
    subprocess.call(["ls", "-1"], shell=False)

# Command with shell expansion
if sys.platform == "win32":
    subprocess.call("echo %USERNAME%", shell=True)
else:
    subprocess.call("echo $HOME", shell=True)

# p = subprocess.Popen(["echo", "hello world"], stdout=subprocess.PIPE)

# print p.communicate()
