#!/usr/bin/python
"""
Purpose: classes (OOP) introduction

    classes 
        1. old style classes - python 2 
            class - type - class object 
        2. new style classes - python 2 & 3

PEP 8 -> class names should be in CamelCasing
"""


# Class Definition
class EmptyClass:
    pass


# Instantiation
e1 = EmptyClass()
print(f'e1:{e1} {type(e1)}')


# -----------------------------------------
class MyClassName:
    number = 786  # class variable

    def hello_world(self):  # Methods
        return 'Hello world'


# Instantiation
c1 = MyClassName()
print(f'c1:{c1} {type(c1)}')
print(dir(c1))

print(f'callable(c1.number)     :{callable(c1.number)}')
print(f'c1.number               :{c1.number}')

print(f'callable(c1.hello_world):{callable(c1.hello_world)}')
print(f'c1.hello_world          :{c1.hello_world}')
print(f'c1.hello_world()        :{c1.hello_world()}')

print()  # check  for user-defined objects
print(f'isinstance(c1, MyClassName):{isinstance(c1, MyClassName)}')
print(f'isinstance(c1, EmptyClass) :{isinstance(c1, EmptyClass)}')
print(f'isinstance(e1, EmptyClass) :{isinstance(e1, EmptyClass)}')

print()  # Check for builtin objects
print(f'isinstance(123, int)        :{isinstance(123, int)}')
print(f'isinstance(123.9, int)      :{isinstance(123.9, int)}')
print(f'isinstance(123.9, float)    :{isinstance(123.9, float)}')
print(f'isinstance(123.9, str)      :{isinstance(123.9, str)}')

num1 = 123
print(f'type(num1) is int:{type(num1) is int}')
isinstance(num1, int)