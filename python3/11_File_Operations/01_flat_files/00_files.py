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

fo.write('\nsomething This is first line ')

print("Closed or not : ", fo.closed)
fo.close()
print("Closed or not : ", fo.closed)

# fo.write('This is first line') # ValueError: I/O operation on closed file.

g = open('foo.txt', 'r')
# g.write('something') #io.UnsupportedOperation: not writable
# print(dir(g))

data  = g.read()
print('data:', data)
g.close()


my_file_handler = open('foo.txt', 'a')
my_file_handler.write('\nAdded in append mode')
my_file_handler.close()

# r+, w+, a+
g = open('foo.txt', 'r+')
g.write('something') 
data  = g.read()
print('data:', data)
g.close()
