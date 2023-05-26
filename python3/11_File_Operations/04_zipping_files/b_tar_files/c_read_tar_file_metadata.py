"""
Purpose: Working with tar files
"""
import os
import tarfile
import time

os.makedirs("files", exist_ok=True)
os.chdir("files")

for file_name in ("fileThree.txt", "tarFileOne.tar", "some.txt"):
    try:
        is_tar_file = tarfile.is_tarfile(file_name)
        print(file_name, "\t", is_tar_file)

        if is_tar_file:
            t = tarfile.open(file_name, "r")
            print("\tFiles in TAR file:", t.getnames())

            print("\n\tMeta Data about that tarfile")
            for info in t.getmembers():
                print(info.name)
                print("\tModified:", time.ctime(info.mtime))
                print("\tMode    :", oct(info.mode))
                print("\tType    :", info.type)
                print("\tSize    :", info.size, "bytes")

    except IOError as err:
        print(err)
