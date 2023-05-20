#!/usr/bin/python3
"""
Purpose: File Operations
"""
import os

# Method 1 - using os.popen()
# popen() provides a pipe/gateway and accesses the file directly
file_handler = os.popen("testfile.txt", "w")
file_handler.write("this is first line")
file_handler.write("this is second line")

# # File not closed, shown in next function.
# os.close(file_handler)


# Method 2
file_handler = open("testfile.txt", "w")
file_handler.write("this is first line\n")
file_handler.write("this is second line\n")
file_handler.close()

file = open("testfile.txt", "r")
text = file.read()
print(text)

# Method 3
file_handler = open("testfile.txt", "w")
print("this is first line\n", file=file_handler)
print("this is second line\n", file=file_handler)
file_handler.close()

# Renaming the file
os.rename("testfile.txt", "mytestfile.txt")
