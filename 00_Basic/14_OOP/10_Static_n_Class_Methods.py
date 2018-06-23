#!/usr/bin/python
# Default Decorators: @staticmethod, @classmethod

class MyClass(object):
    def display(self, x):
        print "executing instance method display(%s,%s)" % (self, x)

    @classmethod
    def cmDisplay(cls, x):
        print "executing class method display(%s,%s)" % (cls, x)

    @staticmethod
    def smDisplay(x):
        print "executing static method display(%s)" % x


a = MyClass()
a.display('Django')  # accessing instance method

MyClass.cmDisplay('Django')  # accessing class method

a.smDisplay('Django')  # accessing static method

MyClass.smDisplay('Django')  # accessing static method
