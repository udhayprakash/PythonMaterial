#!/usr/bin/python
"""Purpose: Calculator Application
"""
__author__ = ''


class Calculate(object):
    def add(self, x, y):
        return x + y

    def mul(self, n1, n2):
        return n1 * n2

if __name__ == '__main__':
    calc = Calculate()
    result = calc.add(2, 2)
    print(result)
