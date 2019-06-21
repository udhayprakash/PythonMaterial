#!/usr/bin/python

'''
file operations 
    - read  - r
    - write - w
    - append- a

    default is read mode
'''
# # Open a file
fo = open("foo.txt", 'w')
print("Name of the file: ", fo.name)
print("Opening mode : ", fo.mode)

fo.write('This is first line')
fo.flush()
print("Closed or not : ", fo.closed)
fo.close()
print("Closed or not : ", fo.closed)


# fo.write('This is first line') # ValueError: I/O operation on closed file.

g = open("foo.txt", 'w')
g.write('This is second line\n')

g.flush()
g.close()

fh = open("foo.txt", 'a')
print('fh.writable()', fh.writable())
fh.write('This is third line\n')
fh.flush()
fh.close()


f_h = open('foo.txt', 'r')
print('f_h.writable()', f_h.writable())
# f_h.write('This is third line\n') # io.UnsupportedOperation: not writable
print('f_h.readable()', f_h.readable())
file_content = f_h.read()
print('file content \n', file_content)
f_h.flush()
f_h.close()


# r+, w+, a+
g = open('foo.txt', 'r+')
g.write('something') 
data  = g.read()
print('data:', data)
g.close()
