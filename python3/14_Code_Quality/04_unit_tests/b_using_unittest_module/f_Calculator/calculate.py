#!/usr/bin/python
"""Purpose: Calculator Application
"""
__author__ = ""


class Calculate:
    """
    >>> calc = Calculate()
    >>> calc.add(-2, 2)
    0
    >>> calc.mul(-2, 2)
    -4
    """

    def add(self, x, y):
        return x + y

    def mul(self, n1, n2):
        return n1 * n2
