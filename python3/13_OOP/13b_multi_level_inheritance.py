#!/usr/bin/python3
"""
Purpose: 
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


if __name__ == '__main__':
    print(D().func())
    # OUTPUT
    # D
    # C
    # B
    # A
    # 'super' object has no attribute 'func'
