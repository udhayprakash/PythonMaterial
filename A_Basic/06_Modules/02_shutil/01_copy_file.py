from shutil import copyfile
# -*- coding: utf-8 -*-
"""
──────────────────  ───────────────  ──────────────────  ────────────── ─────────── 
     Function       Copies metadata  Copies permissions  Can use buffer Dest dir OK 
──────────────────  ───────────────  ──────────────────  ────────────── ─────────── 
shutil.copy               No                 Yes             No             Yes     
shutil.copyfile           No                 No              No             No      
shutil.copy2              Yes                Yes             No             Yes     
shutil.copyfileobj        No                 No              Yes            No      
──────────────────  ───────────────  ──────────────────  ────────────── ─────────── 
"""
import os
SOURCE_FILE = 'test_dir_1/test_file_1.txt'
DESTINATION_FILE = 'test_dir_2/test_file_1.txt'

if os.path.exists(DESTINATION_FILE):
    print("file already exists. So, deleting")
    os.remove(DESTINATION_FILE)

copyfile(SOURCE_FILE, DESTINATION_FILE)