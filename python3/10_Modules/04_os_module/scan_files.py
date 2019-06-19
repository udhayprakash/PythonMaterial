#!/usr/bin/python
"""
Purpose: scan files
"""
import os
search_path = r'C:\Users\udhayPrakash\Desktop\PythonMaterial\python3'
# print('current dir:', os.getcwd())
# print('dir content:\n')
# for each in os.listdir(search_path):
#     print(each)

# print(os.walk(search_path))
# # dir_path, dirs_in_pth, files_in_path

py_files = []
for each_dir, folders, files in os.walk(search_path):
    for each_file in files:
        file_etn = os.path.splitext(each_file)[1]
        if file_etn == '.py':
            py_files.append(each_file)

print(len(py_files))