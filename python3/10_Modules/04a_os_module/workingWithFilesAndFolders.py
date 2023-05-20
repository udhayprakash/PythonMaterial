#!/usr/bin/python

"""
Purpose : working with files and folders
"""

import os

dirToCheck = input("Enter the directory path to check(dont enclose path with quotes):")

print("dirToCheck", dirToCheck)
print("dirToCheck[0]", dirToCheck[0])

for dirpath, dirnames, filenames in os.walk(dirToCheck):
    print("Current Path:", dirpath)
    print("Directories:", dirnames)
    print("Files:", filenames)
    print("-" * 50)
