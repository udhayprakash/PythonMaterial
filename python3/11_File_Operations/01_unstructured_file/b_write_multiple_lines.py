#!/usr/bin/python
"""
file operations
    - read  - r
    - write - w
    - append- a

    default is read mode
"""
fh = open('other_file.tsf', 'w')

# To write a single line
fh.write('first line\n')

strings = ['first\n', 'second\n', 'third\n', 'fourth\n']
# for each_ele in strings:
#     fh.write(each_ele)

# To write multiple lines
fh.writelines(strings)

# flushing
fh.flush()

# closing the file handler
fh.close()

# Assignment  - fh.writeline
