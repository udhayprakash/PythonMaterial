#!/usr/bin/python

'''
Purpose:  To read data from a file
'''

f = open('test.txt', 'rb')    # opening in read mode

print dir(f)
print 'The first 12 characters in the file are ', f.read(12)
print 'The next 6 characters in the file are \n', f.read(6)

print 'The current position of cursor in file is ', f.tell()
data1 = f.readline()
print 'The current position of cursor in file is ', f.tell()
data = f.read()
print 'The current position of cursor in file is ', f.tell()
data = f.read()
print 'moving the cursor position to 10'
f.seek(10)
print 'The current position of cursor in file is ', f.tell()
data = f.read()
print 'The current position of cursor in file is ', f.tell()
f.close()

print data
