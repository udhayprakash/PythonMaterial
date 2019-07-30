#!/usr/bin/python
"""
Purpose: python syntax and basics
"""

name = "Almighty"

print(name)
print('name')
# print(name1) # NameError: name 'name1' is not defined
# print(name1) # NameError: name 'name1' is not defined
print('name1')

print('\n\tname =', name)

# escape sequences \t \n
print('type(name) =', type(name))

print('Name of the student:', name)
print('Name of the student:' + name)

name = 123
print('type(name) =', type(name))
print('Name of the student:', name)
# print('Name of the student:' + name)
# Python is a strictly typed language

# print(1 + '1')
print(str(1) + '1')
print(1 + int('1'))


# NO difference between single and double quotes in python
print('hello')
print("world")

print('hello', end='\n')
print("world")

print('hello', end='___')
print("world")

print('hello', 'python', sep=' ')
print('hello', 'python', sep='\t')


print('hello', 'python', sep='\t', end='..')
print('world!')


print('one\ttwo\nthree\tfour')


print('He\bi')
print('\u20B9')
print('\046')
print('\x24')
print('\xf1')
print('\u018e')

print('#$%*&^(*')