#!/usr/bin/python
"""
Methods
    1. Instance Methods
    2. class Methods
    3. static Methods

Default Decorators: @staticmethod, @classmethod, @property
"""


class MyClass:
    my_var = "something"  # class variable

    def display(self, x):
        print("executing instance method display(%s,%s)" % (self, x))

    @classmethod
    def cmDisplay(cls, x):
        print("executing class method display(%s,%s)" % (cls, x))

    @staticmethod
    def smDisplay(x):
        print("executing static method display(%s)" % x)
        # neither use instance methods, instance variable, class methods nor class variables


if __name__ == "__main__":
    a = MyClass()

    a.display("Django")  # accessing instance method
    MyClass.display(a, "Django")  # accessing instance method

    a.cmDisplay("Django")  # accessing class method
    MyClass.cmDisplay("Django")  # accessing class method

    a.smDisplay("Django")  # accessing static method
    MyClass.smDisplay("Django")  # accessing static method


class Myclass:
    val = 0

    def __init__(self):
        self.val = 0

    @staticmethod
    def incr(self):
        Myclass.val = Myclass.val + 1


I = Myclass()
print(f"{I.val = }")

I.incr()
print(f"{I.val = }")

Myclass.incr()
