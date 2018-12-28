#!/usr/bin/python
"""
Purpose: classes (OOP) introduction
"""
class EmptyClass:
    pass

class MyClassName:        # class definition
    def hello_world(self):      # method
        return 'hello world'

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

print n.hello_world()
print MyClassName.hello_world(n)