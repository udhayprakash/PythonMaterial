#!/usr/bin/python
"""
Purpose: Importance of context manager


Q) what is the interval at which the garbage collector will check for unreferenced objects
Ans) depends on the system clock cycle
        2.3 GHz
"""
# Method 1: traditional
try:
    fh = open("e_write_multiple_lines.tsf", "r")

    data = fh.read()
    print(data)
finally:
    fh.close()
# fh.read()
# ValueError: I/O operation on closed file.


# Method 2: with context manager
with open("e_write_multiple_lines.tsf", "r") as gh:
    data = gh.read()

print(data)
# gh.read()
# ValueError: I/O operation on closed file.


# -----------------------------------------------
# Method 1: traditionally
gh = open("h_context_manager.txt", "w", encoding="utf_8")
# gh.writelines(['1', '2', '3', '4'])
gh.writelines(["1\n", "2\n", "3\n", "4\n"])
gh.flush()
gh.close()
# gh.write('next') # ValueError: I/O operation on closed file.


# Method 2: Using context manager
with open("h_context_manager.txt", "w", encoding="utf_8") as gh:
    gh.writelines(["1", "2", "3", "4"])

# gh.write('next') # ValueError: I/O operation on closed file.


# NOTE: Even though context manager will close the file handler,
# PEP 8 recommends to close explicitly
