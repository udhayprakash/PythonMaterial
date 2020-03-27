#!/usr/bin/python
"""
Purpose: print syntax and usage
"""
name = 'Almighty'

print(name)
print('name')
print('name', name)

print('Name of the student:' + name)  # str + str = str
print('Name of the student:', name)
print('Name of the student:', name, sep=' ')
print('Name of the student:', name, sep='_')
print('Name of the student:', name, sep='')

print(1, 2, 3, 4, 5, 6)
print(1, 2, 3, 4, 5, 6, sep=' ')
print(1, 2, 3, 4, 5, 6, sep='_')

# Python is dynamic typed language
name = 1232
print('Name of student:', name)
# print('Name of student:' + name)  # str + int
# TypeError: can only concatenate str (not "int") to str

# NOTE: Python is a strictly typed language
print('1 + 1 =', 1 + 1)  # addition
print('1' + "1")  # string concatenation
# both single & double quote strings are same in python

# type converters - str(), int(), float()
print("1 + int('1') =", 1 + int('1'))  # addition
print("str(1) + '1' =", str(1) + '1')  # string concatenation

print("int('234'):", int('234'))
# int('two')
# ValueError: invalid literal for int() with base 10: 'two'

print('Name of student:' + str(name))
print('Name of student:', str(name))
print()
# ------------------------------------
# Escape sequences
# \t - tab space
# \n - new line

print('hello world python')
print('hello \tworld \npython')
print(r'hello \tworld \npython')  # to not consider escape sequences

print()
# --------------------
# print(data, sep=' ', end = '\n')
print('hello')
print('world')

print('hello', end='\n')
print('world')

print('hello', end='__')
print('world')

print('hello', 'python', 123, end='__')
print('world')

print('hello', 'python', 123, sep=',', end='__')
print('world')

print('hello', 'python', 123, sep=';', end='\t')
print('world')

# ----------------------
print('#$%*&^(*')
print('He\bi')
print('\u20B9')
print('\046')
print('\x24')
print('\xf1')
print('\u018e')
