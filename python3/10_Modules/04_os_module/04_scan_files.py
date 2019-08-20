#!/usr/bin/python
"""
Purpose: scan files
"""
import os

path = r'C:\Python27'
# print(os.getcwd())

# print(os.listdir(path))
# print(os.walk(path))

py_files = []
for each_dir, dirs, files in os.walk(path):
    for each_file in files:
        file_etxn = os.path.splitext(each_file)[1]
        if file_etxn == '.py':
            py_files.append(each_file)

print(f'There are {len(py_files)} py files under {path}')
