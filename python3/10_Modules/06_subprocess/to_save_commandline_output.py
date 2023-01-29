# AIM: to place the output of "dir" in command line into a TextFile.txt

import os
import subprocess

print(os.getcwd())

# To execute a command-line output and save in a file
subprocess.call("dir >>newFile.txt", shell=True)

# To output the command output, without saving the result
print(subprocess.check_output("dir", shell=True))


# To check in a particular path
print(subprocess.check_output("dir C:\\Users\\upethakamsetty\Downloads", shell=True))

with open("newFile.txt", "r+b") as f:
    str = f.read()
    print(str)
