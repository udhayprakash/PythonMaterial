#!/usr/bin/python
"""
Purpose:
Take a backup zip file for all files on desktop
"""
from zipfile import ZipFile
import os

file_path = os.environ["USERPROFILE"] + os.sep + "Downloads"
print(f"file_path:{file_path}")

with ZipFile("content.zip", "w") as zp_fh:
    for ech_dir, dirs, files in os.walk(file_path):
        for ech_file in files:
            # print(ech_file)
            zp_fh.write(os.path.join(ech_dir, ech_file))
    zp_fh.close()
