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

    def my_function(self, name, age):  # noqa: F811
        print("Hello World!, two Variable Case!!!")


m = MyNewClass()
# m.my_function('Udhay')
# TypeError: MyNewClass.my_function() missing 1 required positional argument: 'age'
# help(m)

m.my_function("Udhay", 28)


class MyNewClass:
    """
    This is method overwriting
    """

    def my_function(self, name, age):
        print("Hello World!, two Variable Case!!!")

    def my_function(self, name):
        print("Hello World!, One Variable Case!!!")


m2 = MyNewClass()
help(m2)
m2.my_function("Udhay")
# m2.my_function('udhay', 28)
# TypeError: MyNewClass.my_function() takes 2 positional arguments but 3 were given


# case 1 - when both methods are in same class -- go for default args
class MyOverLoadEx:
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
m2.my_over_load_function("Udhay")
m2.my_over_load_function("Udhay", 28)


# case 2 =--- when  both methdos are in different classes, use as private methods
# assignment -
