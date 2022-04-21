#!/usr/bin/python
# fileOperations.py
'''
Purpose: File operations demonstration
'''

# accessing an exising file
f = open('test.txt', 'rb')    # filehandlerObject = open('path/tofile/filename.etxn', 'mode')
# 'f' is the file handler
print f, type(f)


# reading the data present in the test.txt
data = f.read()
print 'data  = ', data


print 'Again trying to print the data from file'
data = f.read()
print 'data  = ', data

print 'The current position of cursor in file is ', f.tell()

print 'moving the cursor position to 0'
f.seek(0)
print 'The current position of cursor in file is ', f.tell()

print 'The first 12 characters in the file are ', f.read(12)

print 'The next 6 characters in the file are \n', f.read(6)

print 'The current position of cursor in file is ', f.tell()

print 'moving the cursor position to 7'
f.seek(7)
print 'The current position of cursor in file is ', f.tell()

print 'The current line in file is \n', f.readline()
print 'The current position of cursor in file is ', f.tell()
print 'The current line in file is \n', f.readline()
print 'The current position of cursor in file is ', f.tell()
print 'checking whether file is closed or not'
print 'return True, if the file is closed:', f.closed

f.close()   # to close a file handler object

print 'checking whether file is closed or not'
print 'return True, if the file is closed', f.closed

try:
    f.read() #No operation can be performed on a closed file object, as the object gets dereferenced
    # garbage collector deletes all the unreferenced objects
except ValueError, ve:
    print ve
    print "IO operation can't be performed on closed file handler"


g = open('test.txt', 'wb')   # opening existing file in read mode will erase its existing data.

try:
    datag = g.read()
    print 'datag = ', datag
except IOError, ex:
    print ex
    print 'opened file in write mode. can not read the data'

g.write('New Python programming is interesting\n')
g.write('It is coming with batteries, in built.')
g.write('It means that almost every operation has a module !')

g.close()  # it is not mandatory , but extremely recommended.
# python interpreter with close the file, but
# IronPython, Jython, ... may not close the file automatically.

print '='*80, '\n', 'USING CONTEXT MANAGER'.center(80),'\n', '='*80
# Using Context manager for file handling

with open('test.txt', 'ab+') as h:
    print 'The cursor position is at %d'%(h.tell())
    dataf = h.read()
    print 'The cursor position is at %d' % (h.tell())
    print 'The content of the data is ', dataf
    # append mode supports both read and write operations
    #h.write('This is last line')
    print 'The cursor position is at %d' % (h.tell())
    h.close()
