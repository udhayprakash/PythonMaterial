from glob import glob
from shutil import copyfile

print("BEFORE:", glob("shutil_copyfile.*"))

copyfile("shutil_copyfile.py", "shutil_copyfile.py.copy")
#  Raises IOError if you do not have permission to write to the destination file.

print("AFTER:", glob("shutil_copyfile.*"))
