#!/usr/bin/python
"""
Purpose: classes (OOP) introduction
"""


class Name:  # class definition
    pass


n = Name()  # instantiation

print 'Name  :', Name
print 'Name():', Name()
print 'n     :', n

print 'type(Name)  :', type(Name)
print 'type(Name()):', type(Name())
print 'type(n)     :', type(n)

print 'isinstance(n, Name) :', isinstance(n, Name)
print "__name__", __name__