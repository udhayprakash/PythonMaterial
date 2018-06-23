#!/usr/bin/python
"""
Purpose: Method Overloading & Method Overwriting demonstration

"""
__author__ = 'Udhay Prakash Pethakamsetty'


class MyNewClass(object):
    """
    This is method overwriting
    """

    def myFunction(self, name):
        print "Hello World!, One Variable Case!!!"

    def myFunction(self, name, age):
        print "Hello World!, two Variable Case!!!"


m = MyNewClass()
# m.myFunction('udhay')
m.myFunction('udhay', 28)


class MyOverLoadEx(object):
    """
    This is overloading ex
    """

    def myOverLoadFunction(self, name, age=None):
        if age:
            print "Hello World!, two Variable Case!!!"
        else:
            print "Hello World!, One Variable Case!!!"


n = MyOverLoadEx()

n.myOverLoadFunction('Udhay')
n.myOverLoadFunction('udhay', 28)
