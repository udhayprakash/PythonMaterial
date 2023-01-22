#!/usr/bin/python
"""
Purpose: Multiple Inheritance

    two parents
    one child

NOTE: All the instance variables must be created in constructor - PEP 8
"""


class MyParent:
    p1_cv = 1

    def __init__(self):
        print("MyParent1 class constructor called")
        self.num1 = 0
        self.num2 = 0

    def hello(self):
        return "Hello MyParent1"

    def addition(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        return self.num1 + self.num2


class MyParent2:
    p2_cv = 2

    def __init__(self):
        print("MyParent2 class constructor called")
        self.num1 = 0
        self.num2 = 0

    def hello(self):
        return "Hello MyParent2"

    def subtraction(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        return self.num1 - self.num2


class MyChild(MyParent, MyParent2):  # MRO depends on the order of inheritance
    def __init__(self):
        MyParent.__init__(self)
        MyParent2.__init__(self)

    def _hello(self):
        return "Hello MyChild"


# Instantiation with child class
ch1 = MyChild()
print("ch1.addition(100, 200)   :", ch1.addition(100, 200))
print("ch1.subtraction(100, 200):", ch1.subtraction(100, 200))

print("ch1.hello() :", ch1.hello())
print("ch1._hello():", ch1._hello())

print(MyChild.__mro__)
# (<class '__main__.MyChild'>, <class '__main__.MyParent'>, <class '__main__.MyParent2'>, <class 'object'>)
# (<class '__main__.MyChild'>, <class '__main__.MyParent2'>, <class '__main__.MyParent'>, <class 'object'>)
