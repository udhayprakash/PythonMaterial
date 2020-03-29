#!/usr/bin/python
"""
Purpose: file Read operations
    fh.read()
    fh.readline()
    fh.readlines()

    fh.tell() - to get the current cursor position
    fh.seek() - to move cursor to a specific position
"""
fh = open('other_file.tsf', 'r')  # default is read mode

print(f'fh.readable()               :{fh.readable()}')
print(f'fh.writable()               :{fh.writable()}')

# To read the complete file
complete_file_content = fh.read()
print(f'type(complete_file_content) :{type(complete_file_content)}')
print(complete_file_content)

print('before fh.tell()', fh.tell())
fh.seek(0)
print('after fh.tell()', fh.tell())

complete_file_content = fh.read()
print(complete_file_content)


print('before fh.tell()', fh.tell())
fh.seek(23)
print('after fh.tell()', fh.tell())

complete_file_content = fh.read()
print(complete_file_content)

print('before fh.tell()', fh.tell())
fh.seek(11)
print('after fh.tell()', fh.tell())

# to read specific no. of character from cursor position
complete_file_content = fh.read(18)
print(complete_file_content)

# To close the file handler
fh.close()
