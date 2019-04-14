#!/usr/bin/python
"""
Purpose: python syntax and basics
"""

name = "Almighty"

print(name)

# print('name of the student')
# print(name)

print('name of the student:', name)
print('name of the student:', 'name')

print(type(name))
print('name of the student:'+ name)

name = 123
print(type(name), name)
print('name of the student:', name)

# Python is a Strictly typed language
# print('name of the student:'+ name)
# TypeError: can only concatenate str (not "int") to str

print('name of the student:'+ str(name))

# print('12' + 13)

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
