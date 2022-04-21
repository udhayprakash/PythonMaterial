# -*- coding: utf-8 -*-
"""
Purpose:
"""
import os
from shutil import copyfile

SOURCE_FILE = "test_dir_1/test_file_1.txt"
DESTINATION_FILE = "test_dir_2/test_file_1.txt"

if os.path.exists(DESTINATION_FILE):
    print("file already exists. So, deleting")
    os.remove(DESTINATION_FILE)

copyfile(SOURCE_FILE, DESTINATION_FILE)
