#!/usr/bin/python

'''
file operations 
    - read  - r
    - write - w
    - append- a

    default is read mode
'''
fh = open('newfile.tsf', 'r')

file_cntent = fh.read()
print(type(file_cntent))
print(file_cntent)

print('fh.tell()', fh.tell())
fh.seek(0)

file_cntent = fh.read()
print(type(file_cntent))
print(file_cntent)

print('fh.tell()', fh.tell())
fh.seek(25)

file_cntent = fh.read()
print(type(file_cntent))
print(file_cntent)

print('fh.tell()', fh.tell())
fh.seek(26)

file_cntent = fh.read(5)
print(type(file_cntent))
print(file_cntent)

file_cntent = fh.readline()
print(type(file_cntent),file_cntent)

file_cntent = fh.readline()
print(type(file_cntent),file_cntent)

print('fh.tell()', fh.tell())
fh.seek(0)
file_cntent = fh.readlines()
print(type(file_cntent),file_cntent)
fh.close()