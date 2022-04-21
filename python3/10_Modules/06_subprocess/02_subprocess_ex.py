import subprocess
import sys

if sys.platform == "win32":
    subprocess.call(["dir", "/x"], shell=True)
else:
    subprocess.call(["ls", "-1"], shell=True)

# Command with shell expansion
if sys.platform == "win32":
    subprocess.call("echo %USERNAME%", shell=True)
else:
    subprocess.call("echo $HOME", shell=True)

# p = subprocess.Popen(["echo", "hello world"], stdout=subprocess.PIPE)

# print p.communicate()
