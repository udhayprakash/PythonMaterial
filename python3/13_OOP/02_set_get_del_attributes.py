#!/usr/bin/python
"""
Purpose: classes (OOP) introduction
"""


# class Definition
class Myclass:
    pass


# Instantiation
m = Myclass()
print(m, type(m))

# To list the attributes
print(dir(m))

# To set an attribute
setattr(m, 'value', 100.23)
m.value2 = 2342
print(dir(m))
# Instances are mutable objects

# To retrieve an attribute
print(f'm.value:{m.value}')
assert getattr(m, 'value') == m.value

# To delete an attribute
delattr(m, 'value')
del m.value2

print(dir(m))
