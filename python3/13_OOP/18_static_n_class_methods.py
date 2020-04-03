#!/usr/bin/python
"""
Methods
    1. Instance Methods
    2. class Methods
    3. static Methods

Default Decorators: @staticmethod, @classmethod
"""


class MyClass:
    my_var = 'something'  # class variable

    def display(self, x):
        print("executing instance method display(%s,%s)" % (self, x))

    @classmethod
    def cmDisplay(cls, x):
        print("executing class method display(%s,%s)" % (cls, x))

    @staticmethod
    def smDisplay(x):
        print("executing static method display(%s)" % x)
        # neither use instance methods, instance variable, class methods nor class variables


a = MyClass()

a.display('Django')  # accessing instance method
MyClass.display(a, 'Django')  # accessing instance method

a.cmDisplay('Django')  # accessing class method
MyClass.cmDisplay('Django')  # accessing class method

a.smDisplay('Django')  # accessing static method
MyClass.smDisplay('Django')  # accessing static method
