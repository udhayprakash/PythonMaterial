#!/usr/bin/python
"""
Purpose: multiple ways of file read operations
    possible modes: r, r+

    fh.read()
    fh.readline()
    fh.readlines()

"""
fh = open('e_write_multiple_lines.tsf', 'r') # default is read mode

print(f'{fh.writable() =}')  # False
print(f'{fh.readable() =}')  # True 


complete_content = fh.read()
print(f'{type(complete_content) =}')
print(f'Initially {complete_content       =}')

complete_content = fh.read()
print(f'Again     {complete_content       =}')

# --------------------------------------------
print('before fh.tell()', fh.tell())
fh.seek(0)
print('after  fh.tell()', fh.tell())

complete_content = fh.read()
print(f'Again     {complete_content       =}')

# ---------------------------------------------
print('before fh.tell()', fh.tell())
fh.seek(29)
print('after fh.tell()', fh.tell())

# reads from cursor position till EOF
partial_content = fh.read() 
print(f'{partial_content = }')

# ---------------------------------------------
print('before fh.tell()', fh.tell())
fh.seek(29)
print('after fh.tell()', fh.tell())

# To read specific no. of character from cursor position
partial_content = fh.read(12)
print(f'\n{partial_content = }')

partial_content = fh.read(6)
print(f'\n{partial_content = }')

fh.close()


# The seek() method accepts two arguments:

# offset – A number of bytes from whence
# whence – The reference point
# You can set whence to these three values:

# 0 – The beginning of the file (default)
# 1 – The current file position
# 2 – The end of the file