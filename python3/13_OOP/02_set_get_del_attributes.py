#!/usr/bin/python
"""
Purpose: classes (OOP) introduction
"""
class MyClass:
    pass

m = MyClass()
print(m)
print(dir(m))

setattr(m, 'value', 100.23)

print(getattr(m, 'value'))
print(m.value)

delattr(m, 'value')
# print(m.value)AttributeError: 'MyClass' object has no attribute 'value'
