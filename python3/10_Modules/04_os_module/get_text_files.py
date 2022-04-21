#!/usr/bin/python
"""
Problem: Let's take a look around the current
  directory and find all the .txt files inside it.
"""
import os

print(f"There are {os.cpu_count()} CPU's in this system.")

print(f'Here is a proper 200-byte random number: {str(os.urandom(200))}.')

names = os.listdir('.')
print(f"The current directory is: {os.path.abspath('.')}")
print(f'The current directory contains {len(names)} filenames.')
for name in names:
    if os.path.isfile(name) and name.endswith('.txt'):
        st = os.stat(name)  # an os.statresult object
        print(f'Found text file {name} of {st.st_size} bytes.')
        print(f'This file was last modified at time {st.st_mtime}.')
