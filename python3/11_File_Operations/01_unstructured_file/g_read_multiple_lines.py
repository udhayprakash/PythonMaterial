#!/usr/bin/python
"""
Purpose: file read operations
    fh.read()
    fh.readline()
    fh.readlines()
"""
fh = open("e_write_multiple_lines.upp", "r")


partial_content = fh.read(7)
print(f"{partial_content  =}")  # str type

# --------------------------------------------
print("\ncurrent  fh.tell()", fh.tell())

# TO read current line, from cursor position, till end of line
current_line = fh.readline(5_000_000)  # -> str
print(f"\n{type(current_line) =}")  # str type
print(f"{current_line       =}")

print("\ncurrent  fh.tell()", fh.tell())
current_line = fh.readline(5_000_000)  # -> str
print(f"{current_line       =}")


# ----------------------------------------------
print("\ncurrent  fh.tell()", fh.tell())
# To read all lines, from cursor position, till end of file (EOF)
multiple_lines = fh.readlines()  # -> list
print(f"{type(multiple_lines) =}")
print(f"{multiple_lines       =}")


fh.close()
