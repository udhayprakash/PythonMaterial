#!/usr/bin/python
"""
Purpose: python syntax and basics
"""

name = "Almighty"

print(name)
print('name')
# print(name1) # NameError: name 'name1' is not defined

print('\n\tname =', name)
print(type(name), name)

print('name of student: name')
print('name of student:', name)
print('name of student:' +  name)

name = 123
print('\n', type(name), name)
print('name of student:', name)
# print('name of student:' +  name)
# # TypeError: can only concatenate str (not "int") to str

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

print('Hello', 'udhay', 'third', sep='|',end='_')
print("world")

print("Hello","World", sep="***")        # Hello***World
print("Hello","World", end="***")        # Hello World***
print("Hello", end="***"); print("World")# Hello***World

print('one\ttwo\nthree\tfour')

print('He\bi')
print('\u20B9')
print('\046')
print('\x24')
print('\xf1')
print('\u018e')

print('#$%*&^(*')