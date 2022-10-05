#!/usr/bin/python3
"""
Purpose: File Pattern Matching using glob module
"""
import glob
import os
import sys

print(f"{sys.exec_prefix =}")
os.chdir(sys.exec_prefix)

print("\n Current Directory")
text_files = glob.glob("*.txt")
for each_txt_file in text_files:
    print("\t", each_txt_file)

print("\n One Level Deep")
text_files = glob.glob("*/*.txt")
for each_txt_file in text_files:
    print("\t", each_txt_file)

print("\n Two Levels Deep")
text_files = glob.glob("*/*/*.txt")
for each_txt_file in text_files:
    print("\t", each_txt_file)

print("\n Three Levels Deep")
text_files = glob.glob("*/*/*/*.txt")
for each_txt_file in text_files:
    print("\t", each_txt_file)

print("\n All levels Deep (as available)")
text_files = glob.glob("**/*.txt", recursive=True)
for each_txt_file in text_files:
    print("\t", each_txt_file)
