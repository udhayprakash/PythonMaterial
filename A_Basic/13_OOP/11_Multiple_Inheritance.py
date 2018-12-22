#!/usr/bin/python
"""
Purpose: Multiple Inheritance
"""


class MyParent1:  # (object):
    p1_cv = 1

    def __init__(self):
        print "MyParent1 class constructor called"

    def hello(self):
        return "Hello MyParent1"

    def addition(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

        self.result = self.num1 + self.num2


class MyParent2:  # (object):
    p2_cv = 2

    def __init__(self):
        print "MyParent2 class constructor called"

    def hello(self):
        return "Hello MyParent2"

    def subtraction(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

        self.result = self.num1 - self.num2


class MyChild(MyParent2, MyParent1):
    def __init__(self):
        MyParent1.__init__(self)
        MyParent2.__init__(self)
        # super.__init__(self)


# Instantiation
ch = MyChild()

print dir(ch)
print ch.hello()
