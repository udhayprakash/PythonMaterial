#!/usr/bin/python
"""
Purpose:
    file operations
        - read  - r
        - write - w -> if file not present, file will be created; 
                       if present, existing content will be overwritten
        - append- a

        default is read mode
"""

fh = open('myfile.txt', 'w')
fh.write('This is first line')


print("Name of the file: ", fh.name)
print("Opening mode    : ", fh.mode)

fh.flush()

print("Closed or not    : ", fh.closed)
fh.close()  # garbage collector
print("Closed or not    : ", fh.closed)

# fh.write('fh world 3 !\n')
# ValueError: I/O operation on closed file.

g = open("myfile.txt", 'w')
g.write('This is second line\n')
g.flush()
g.close()


fh = open("myfile.txt", 'a')

print('fh.writable()   :', fh.writable()) # True
print('fh.readable()   :', fh.readable()) # False

fh.write('This is third line\n')
fh.flush()
fh.close()

f_h = open('myfile.txt', 'r')

print('f_h.writable()  :', f_h.writable()) # Fale
# f_h.write('This is third line\n') # io.UnsupportedOperation: not writable

print('f_h.readable()  :', f_h.readable()) # True
file_content = f_h.read()
print('file content \n', file_content)

f_h.close()


# ----------------------

# r+, w+, a+
g = open('myfile.txt', 'r+')

print('g.writable()   :', g.writable()) # True
g.write('something')

print('g.readable()   :', g.readable()) # True
data = g.read()
print('data:', data)


g.close()