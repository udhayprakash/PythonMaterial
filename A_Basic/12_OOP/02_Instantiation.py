#!/usr/bin/python
"""
Purpose: classes (OOP) introduction
"""


class MyClassName:        # class definition
    def hello(self):      # method
        print 'hello world'

n = MyClassName()         # Instantiation
print 'n            :', n

print 'MyClassName  :', MyClassName
print 'MyClassName():', MyClassName()
print
print 'type(MyClassName)  :', type(MyClassName)
print 'type(MyClassName()):', type(MyClassName())
print 'type(n)            :', type(n)
print
print 'isinstance(n, MyClassName) :', isinstance(n, MyClassName)
print 'isinstance(1, MyClassName) :', isinstance(1, MyClassName)
print "__name__", __name__

print
n.hello()  
MyClassName.hello(n)