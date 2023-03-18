#!/usr/bin/python
"""
Purpose: __repr__
"""


class TheProblem:
    def __init__(self, items):
        self.items = list(items)

    def __repr__(self):
        items = self.items
        return f"{items}"

    # def __str__(self):
    #     return 'str is called'

    __str__ = __repr__


# NOTE: print will call __str__ if present, else __repr__

p1 = TheProblem(range(50))
print(p1)  # str is called

print(
    f"{p1 =}"
)  # p1 =[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
print()
# -----------------------------------------
import reprlib


class Solution:
    def __init__(self, items):
        self.items = list(items)

    def __repr__(self):
        items = reprlib.repr(self.items)
        return f"{items}"


p2 = Solution(range(50))
print(p2)


# --------------------------------------------
class Foo(object):
    def __str__(self):
        return "Testing"

    def __repr__(self):
        return "Programming"


print("{!s} {!r}".format(Foo(), Foo()))
print("{0!s} {0!r}".format(Foo()))
