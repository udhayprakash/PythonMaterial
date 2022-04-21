#!/usr/bin/python3
"""
Purpose: Multiple and Multi-Level Inheritance
"""


class A:
    def func(self):
        print('A')
        super().func()


class B(A):
    def func(self):
        print('B')
        super().func()


class C(A):
    def func(self):
        print('C')
        super().func()


class D(C, B):
    def func(self):
        print('D')
        super().func()


class E(D, A):
    def func(self):
        print('E')
        super().func()


print(D().func())
# OUTPUT
# D
# C
# B
# A
# 'super' object has no attribute 'func'


# ===============================================

class P1:
    def __init__(self, val):
        print("P1 val =", val)


class P2:
    def __init__(self, val):
        print("P2 val =", val)


class C1(P1, P2):
    def __init__(self, val):
        print("c1 val =", val)

        # It will call only once constructor, as per MRO
        super().__init__(val)

        # To explicitly call one or more parent constructors,
        P1.__init__(self, val)
        P2.__init__(self, val)

        # NOTE: use either, but not both


c = C1(10)
