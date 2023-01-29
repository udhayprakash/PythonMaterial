# Let's say you have a file structure like this:

# zips
# |-- newyork
# |    |-- normal
# |    |    |-- a
# |    |    |-- b
# |    |    +-- c
# |    +-- pressed
# |         |-- a
# |         |-- b
# |         +-- c
# +-- chicago
#     |-- normal
#     |    |-- a
#     |    |-- b
#     |    +-- c
#     +-- pressed
#          |-- a
#          |-- b
#          +-- c
#

#!/usr/bin/env python

import os
import zipfile

# these folders were retrieved dynamically
folders_to_zip = [
    "C:\\Users\\upethakamsetty\Downloads\Shareit\LG-P715\Documents\external_SD",
    "C:\\Users\\upethakamsetty\Downloads\python (2).jpg",
    "C:\\Users\\upethakamsetty\Desktop\\udhay",
]
# loop through all the folders to zip
for folder in folders_to_zip:
    print(("processing: " + folder))
    # concatenate the folders for file name
    zipfilename = "%s.zip" % (folder.replace("/", "_"))
    zfile = zipfile.ZipFile(
        os.path.join(folder, zipfilename), "w", zipfile.ZIP_DEFLATED
    )
    # rootlen => zipped files don't have a deep file tree
    rootlen = len(folder) + 1
    for base, dirs, files in os.walk(folder):
        for file in files:
            fn = os.path.join(base, file)
            zfile.write(fn, fn[rootlen:])
    zfile.close()
