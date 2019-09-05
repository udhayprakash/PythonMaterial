#!/usr/bin/python
"""
Purpose: classes (OOP) introduction
"""
class MyClass:
    pass

m = MyClass()
print(m)
# print(dir(m))

# Using bult-in functions
setattr(m, 'value', 100.23)
# print(dir(m))
print(getattr(m, 'value'))

delattr(m, 'value')
# print(getattr(m, 'value'))  # AttributeError: 'MyClass' object has no attribute 'value'

#--------------------
# Directly accessing based
m.value1 = 123
print(m.value1)

del m.value1
# print(m.value1)  # AttributeError: 'MyClass' object has no attribute 'value1'


m.nirmal = 23
print(dir(m))
