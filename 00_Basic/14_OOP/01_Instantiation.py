#!/usr/bin/python
"""
Purpose: classes (OOP) introduction
"""


class Name:  # class definition
    def hello(self):
        print 'hello world'


n = Name()  # instantiation

print 'Name  :', Name
print 'Name():', Name()
print 'n     :', n
print
print 'type(Name)  :', type(Name)
print 'type(Name()):', type(Name())
print 'type(n)     :', type(n)
print
print 'isinstance(n, Name) :', isinstance(n, Name)
print 'isinstance(1, Name) :', isinstance(1, Name)
print "__name__", __name__

print 
n.hello()