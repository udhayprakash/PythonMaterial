#!/usr/bin/python
"""
Purpose: Method Overwriting
    If two methods are present with same name, python will
    overwrite the latest in the backend
"""


class MyNewClass(object):
    """
    This is method overwriting
    """

    def my_function(self, name):
        print("Hello World!, One Variable Case!!!")

    def my_function(self, name, age):
        print("Hello World!, two Variable Case!!!")


m = MyNewClass()
# m.my_function('Udhay')
# TypeError: my_function() missing 1 required positional argument: 'age'
m.my_function('Udhay', 28)


class MyOverLoadEx(object):
    """
    This is overloading ex

    Duck typing - the language doesn't support a feature,
                    but we implement by some workaround
    """

    def my_over_load_function(self, name, age=None):
        if age:
            print("Hello World!, two Variable Case!!!")
        else:
            print("Hello World!, One Variable Case!!!")


m2 = MyOverLoadEx()
m2.my_over_load_function('Udhay')
m2.my_over_load_function('Udhay', 28)
