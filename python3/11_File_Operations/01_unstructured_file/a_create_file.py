#!/usr/bin/python
"""
Purpose:
    file operations
        - read  - r
        - write - w
        - append- a

        default is read mode
"""
fh = open('my_file.txt', 'w')
fh.write('This is first line')

print("Name of the file: ", fh.name)
print("Opening mode    : ", fh.mode)

fh.flush()

print("Closed or not    : ", fh.closed)
fh.close()  # garbage collector
print("Closed or not    : ", fh.closed)

# fh.write('fh world 3 !\n')
# ValueError: I/O operation on closed file.

g = open("my_file.txt", 'w')
g.write('This is second line\n')
g.flush()
g.close()


fh = open("my_file.txt", 'a')
print('fh.writable()   :', fh.writable())
print('fh.readable()   :', fh.readable())

fh.write('This is third line\n')
fh.flush()
fh.close()

# ----------------------

f_h = open('my_file.txt', 'r')
print('f_h.writable()  :', f_h.writable())
# f_h.write('This is third line\n') # io.UnsupportedOperation: not writable

print('f_h.readable()', f_h.readable())
file_content = f_h.read()
print('file content \n', file_content)

f_h.close()

# ----------------------

# r+, w+, a+
g = open('my_file.txt', 'r+')
g.write('something')
data = g.read()
print('data:', data)
g.close()