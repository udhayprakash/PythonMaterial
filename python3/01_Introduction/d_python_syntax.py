#!/usr/bin/python
"""
Purpose: python syntax and basics
"""

name = "Almighty"

print(name)
print('name')

print('\n\tname =', name)
print(type(name), name)

print('name of student: name')
print('name of student:', name)
print('name of student:' +  name)

name = 123
print('\n', type(name), name)
print('name of student:', name)
# print('name of student:' +  name)
# TypeError: can only concatenate str (not "int") to str

# Python is strictly typed language 
# print('1' + 1)
# TypeError: can only concatenate str (not "int") to str

# no difference between single and double quotes
# for strings
print('hello')
print("world")

print('hello', end='\n')
print("world")

print('hello', end=' ')
print("world")


print('Hello', 'udhay', end='_')
print("world")

