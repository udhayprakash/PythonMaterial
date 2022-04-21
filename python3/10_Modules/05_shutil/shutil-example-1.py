# File: shutil-example-1.py

import shutil
import os


# copy function copies a file in pretty much the same way as the Unix cp command.

targetDirectoryPath = "pyDemo/Demo Programs"

for file in os.listdir("."):
    if os.path.splitext(file)[1] == ".py":
        print(file)
        shutil.copy(file, os.path.join(targetDirectoryPath, file))
