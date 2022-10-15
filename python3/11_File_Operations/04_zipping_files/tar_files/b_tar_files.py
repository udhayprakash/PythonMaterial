import tarfile
from os.path import join as path_join
from os.path import normpath
from pathlib import Path

# creating files
open("fileOne.txt", "w").write("This is first line")
open("fileTwo.txt", "w").write("This is second line")
open("fileThree.txt", "w").write("This is third line")

# Creating new archives
with tarfile.open("tarFileOne.tar", mode="w") as tF:
    tF.add("fileOne.txt")
    tF.add("fileTwo.txt")

# Appending to existing archive
with tarfile.open("tarFileOne.tar", mode="a") as tF:
    tF.add("fileThree.txt")

# deleting existing files
import os

os.remove("fileOne.txt")
os.remove("fileTwo.txt")
os.remove("fileThree.txt")

# # Extracting a specific file from archive
# with tarfile.open("tarFileOne.tar") as tF:
#     tF.extract("fileThree.txt")
# NOTE:  The extract() method does not take care of several extraction issues.
#      In most cases you should consider using the extractall() method.

# Extracting all files in archive
with tarfile.open("tarFileOne.tar") as tF:
    tF.extractall()
