#!/usr/bin/python
"""
Purpose: python syntax and basics
"""

name = "Almighty"

print(name)

print("Name of the student:", name)
# , (comma) logic separator operator

# Python is a strictly typed language
# content of either side of + should be of 
# same data type
print("Name of the student:" + name)

name = 123
print("Name of the student:", name)
# , (comma) logic separator operator
# print("Name of the student:"+ name) # TypeError: cannot concatenate 'str' and 'int' objects
print("Name of the student:"+ str(name))

# print '12' + 34
# Question: strictly typed language

# no difference between single and double quotes
# for strings

print('Hello')
print('world')

# print 'hello', 
print('Hello', end=' ')
print('world')

print('Hello !!!', 'udhay', end=' ') 
print('world')
