#!/usr/bin/python
"""
Purpose: reading existing file
    - If file is not present, it throws an error
"""
fh1 = open("b_create_file.txt", mode="r", encoding="utf-8")

print("Name of the file : ", fh1.name)
print("Opening mode     : ", fh1.mode)

print(f"{fh1.writable() =}")
# fh1.write('This is fifth line\n')
# io.UnsupportedOperation: not writable

print(f"{fh1.readable() =}")

file_content = fh1.read()
print(f"{file_content =}")

fh1.close()

try:
    fh1.read()
except ValueError as ve:
    print(ve)
    print("can not do operations(read/write) on closed file")
