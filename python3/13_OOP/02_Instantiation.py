#!/usr/bin/python
"""
Purpose: classes (OOP) introduction

    classes 
        1. old style classes - python 2 
            class - type - class object 
        2. new style classes - python 2 & 3

PEP 8 -> class names should be in camelCasing    
"""
# class definition
class EmptyClass:
    pass


# Instantiation
e1 = EmptyClass()
print(f'e1:{e1} {type(e1)}')


# class definition
class MyClassName:
    number = 786                # class variables

    def hello_world(self):      # Methods
        return "Hello world"


c1 = MyClassName
print(c1, type(c1))

c1 = MyClassName()
print(c1, type(c1))

print(f'isinstance(c1, MyClassName):{isinstance(c1, MyClassName)}')
print(f'isinstance(e1, MyClassName):{isinstance(e1, MyClassName)}')
print(f'isinstance(e1, EmptyClass) :{isinstance(e1, EmptyClass)}')

print(dir(c1))

print(f'c1.number     :{c1.number}')
print(f'c1.hello_world:{c1.hello_world}')

print(MyClassName.hello_world(c1))
print(c1.hello_world())