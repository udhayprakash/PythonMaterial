#!/usr/bin/python3
"""
Purpose: scan files
"""
import os

path = r"C:\Users\udhayPrakash\AppData\Local\Programs\Python\Python37"


# print(os.getcwd())
# print(os.listdir())

# print(os.listdir(path))
# print(os.walk(path))


def scan_files_by_extn(given_file_etxn, _path):
    files_with_given_extn = []
    for ech_dir, list_of_dirs, list_of_file in os.walk(_path):
        for ech_file in list_of_file:
            file_etxn = os.path.splitext(ech_file)[1]
            if file_etxn == given_file_etxn:
                files_with_given_extn.append(ech_file)

    print(f"There are {len(files_with_given_extn)} py files under {path}")


scan_files_by_extn(".py", path)

# NOTE: os.walk(PATH, topdown=False) will walk from down to top
