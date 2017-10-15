#!/usr/bin/python
# Default Decorators: @staticmethod, @classmethod

class myClass(object):
    def display(self,x):
        print "executing instance method display(%s,%s)"%(self,x)

    @classmethod
    def cmDisplay(cls,x):
        print "executing class method display(%s,%s)"%(cls,x)

    @staticmethod
    def smDisplay(x):
        print "executing static method display(%s)"%x

a = myClass()
a.display('Django')             # accessing instance method

myClass.cmDisplay('Django')     # accessing class method

a.smDisplay('Django')           # accessing static method

myClass.smDisplay('Django')     # accessing static method
