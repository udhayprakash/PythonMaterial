#!/usr/bin/python
"""
file operations
    - read  - r
    - write - w
    - append- a

    default is read mode
"""

fh = open('something.tsf', 'w')

# To write a single line
fh.write('first line\n')

lines = ['second\n', 'third\n', 'fouth\n', 'fifth']
# Method 1 - To write multiple lines
# for each in lines:
#     fh.write(each)

# Method 2 - To write multiple lines
fh.writelines(lines)  # it excepts iteratable of strings

# closing the file handler
fh.close()