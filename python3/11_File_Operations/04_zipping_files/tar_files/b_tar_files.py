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
    def is_within_directory(directory, target):
        
        abs_directory = os.path.abspath(directory)
        abs_target = os.path.abspath(target)
    
        prefix = os.path.commonprefix([abs_directory, abs_target])
        
        return prefix == abs_directory
    
    def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
    
        for member in tar.getmembers():
            member_path = os.path.join(path, member.name)
            if not is_within_directory(path, member_path):
                raise Exception("Attempted Path Traversal in Tar File")
    
        tar.extractall(path, members, numeric_owner=numeric_owner) 
        
    
    safe_extract(tF)
