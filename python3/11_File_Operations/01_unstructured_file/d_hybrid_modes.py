#!/usr/bin/python
"""
Purpose: hybrid file operation modes
    r+, w+, a+
"""
# r+ -> ensure that file is already present
gh = open("b_second_file.txt", "r+")

print(f"{gh.name       =}")
print(f"{gh.mode       =}")

print(f"{gh.writable() =}")
gh.write("This is written in r+ mode")
gh.flush()

print(f"{gh.readable() =}")
file_content = gh.read()
print(f"{file_content =}")

gh.close()

# -------------------------------------------------
print("-" * 10)

# w+ -> removes existing content in file if present
gh = open("d_hybrid_modes.txt", "w+")

print(f"{gh.name       =}")
print(f"{gh.mode       =}")

print(f"{gh.writable() =}")
gh.write("This is written in w+ mode")
gh.flush()

print(f"{gh.readable() =}")
file_content = gh.read()
print(f"Default      : {file_content =}")

# Moving cursor to start of file
gh.seek(0)
file_content = gh.read()
print(f"after seek(0): {file_content =}")

gh.close()


"""
NOTE:

    r+  --- file should present
    w+  ---   write/read
    a+  ---  append/read
"""
