import os
import subprocess
import sys

# subprocess.Popen is more general than subprocess.call.
# Popen doesn't block, allowing you to interact with the
# process while it's running, or continue with other things
# in your Python program; whereas call does block.

if sys.platform in ("linux", "linux2", "darwin"):
    cmd = "ifconfig"
    os.system(cmd)
    subprocess.call(cmd, shell=False)
    myprocess = subprocess.Popen(cmd, shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    output, err = myprocess.communicate()
    print("output==============\n", output)
    print("err=================\n", err)
elif sys.platform == "win32":
    # print(os.system('dir /x C:\Python27'))
    # print(call('dir /x C:\Python27', shell=True))

    myprocess = subprocess.Popen(r"diras /x C:\Python27", shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output, err = myprocess.communicate()
    print("output==============\n", output.decode("utf-8"))
    print("err=================\n", err.decode("utf-8"))
else:
    print("unhandled platform :", sys.platform)
    exit(1)
