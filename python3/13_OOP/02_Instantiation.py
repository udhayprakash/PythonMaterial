#!/usr/bin/python
"""
Purpose: classes (OOP) introduction

    classes 
        1. old style classes - python 2 
            class - type - class object 
        2. new style classes - python 2 & 3
            
"""
class EmptyClass:
    pass

class MyClassName:        # class definition
    number = 786                # class variable
    def hello_world(self):      # method
        return 'hello world'

n = MyClassName()         # Instantiation
print('n            :', n)

print('MyClassName  :', MyClassName)
print('MyClassName():', MyClassName())
print()
print('type(MyClassName)  :', type(MyClassName))
print('type(MyClassName()):', type(MyClassName()))
print('type(n)            :', type(n))
print()
print('isinstance(n, MyClassName) :', isinstance(n, MyClassName))
print('isinstance(1, MyClassName) :', isinstance(1, MyClassName))
print("__name__", __name__)

print('dir(n)', dir(n))

print('\n', n.hello_world())
print(MyClassName.hello_world(n))

print('n.number', n.number)