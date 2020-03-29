#!/usr/bin/python
"""
Purpose: file read operations

    fh.read()
    fh.readline()
    fh.readlines()
"""
fh = open('other_file.tsf', 'r')

complete_content = fh.read(7)  # -> str
print(f'type(complete_content)  :{type(complete_content)}')
print(complete_content)

# TO read current line, from cursor position, till end of line
current_line = fh.readline()  # -> str
print(f'type(current_line)      :{type(current_line)}')
print(current_line)

current_line = fh.readline()  # -> str
print(f'type(current_line)      :{type(current_line)}')
print(current_line)

# To read all lines, from cursor position, till end of file (EOF)
multiple_lines = fh.readlines()  # -> list
print(f'type(multiple_lines)    :{type(multiple_lines)}')
print(multiple_lines)
