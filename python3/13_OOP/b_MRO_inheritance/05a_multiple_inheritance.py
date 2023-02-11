#!/usr/bin/python
"""
Purpose: Multiple Inheritance

    two parents
    one child

NOTE: All the instance variables must be created in constructor - PEP 8
"""


class A:
    def __init__(self):
        print("A")
        super(A, self).__init__()
        print("<A>")


class B:
    def __init__(self):
        print("B")
        super(B, self).__init__()
        print("<B>")


class C(A, B):
    def __init__(self):
        print("C")
        super(C, self).__init__()
        print("<C>")


C()
