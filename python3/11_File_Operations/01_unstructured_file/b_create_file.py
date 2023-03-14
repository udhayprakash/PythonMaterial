#!/usr/bin/python
"""
Purpose: creating file and adding content
"""
fh = open("b_create_file.txt", mode="w", encoding="utf-8")

print("Name of the file : ", fh.name)
print("Opening mode     : ", fh.mode)
print("Softspace flag   : ", fh.softspace)

fh.write("This is first line\n")
fh.write("This is second line\n")
fh.flush()

print("Closed or not    : ", fh.closed)
fh.close()  # garbage collector
print("Closed or not    : ", fh.closed)

try:
    fh.write("This is third line\n")
except ValueError as ve:
    print(ve)
    print("can not do operations(read/write) on closed file")


# ---- REOPENING the same file in write mode
gh = open("b_create_file.txt", mode="w", encoding="utf-8")
gh.write("This is third line\n")

gh.flush()
gh.close()

# NOTE:
# 1. In write mode, if file is not present, new file is created and content is added
# 2. IN write mode, if file present, removes existing content and adds new content.


# ----Adding content to existing file
mh = open("b_create_file.txt", mode="a")
mh.write("This is fourth line\n")

mh.flush()
mh.close()


# The truncate() method resizes the file to the given number of bytes.
f = open("b_create_file.txt", "a")
f.truncate(20)
f.close()

# open and read the file after the truncate:
f = open("b_create_file.txt", "r")
print(f.read())
