#!/usr/bin/python
"""
Purpose: classes (OOP) introduction
"""


class MyClassName:        # class definition
    def hello(self):      # class method
        print 'hello world'


n = MyClassName()                # Instantiation

print 'MyClassName  :', MyClassName
print 'MyClassName():', MyClassName()
print 'n            :', n
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