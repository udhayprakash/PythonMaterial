import os
from shutil import *

if not os.path.exists("example"):
    os.mkdir("example")

print("BEFORE:", os.listdir("example"))
copy("shutil_copyfile.py", "example")
print("AFTER:", os.listdir("example"))
