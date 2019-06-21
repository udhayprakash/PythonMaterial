#!/usr/bin/python

'''
file operations 
    - read  - r
    - write - w
    - append- a

    default is read mode
'''
fh = open('newfile.tsf', 'r')

data = fh.read()
print(type(data))
print(data)

print('fh.tell()', fh.tell())
fh.seek(0)

data = fh.read()
print(type(data))
print(data)

print('fh.tell()', fh.tell())
fh.seek(25)

data = fh.read()
print(type(data))
print(data)

print('fh.tell()', fh.tell())
fh.seek(26)

data = fh.read(5)
print(type(data), data)

data = fh.readline()
print(type(data),data)

data = fh.readline()
print(type(data),data)

print('fh.tell()', fh.tell())
fh.seek(0)
data = fh.readlines()
print(type(data),data)

fh.close()