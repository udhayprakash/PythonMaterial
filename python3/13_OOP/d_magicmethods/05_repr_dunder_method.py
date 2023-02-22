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


p1 = TheProblem(range(50))
print(p1)  # __repr__
# NOTE: when both __str__ and __repr__ were present,
# for print, __str__ will be preferred

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


print("{!s} {!r}".format(Foo()))
print("{0!s} {0!r}".format(Foo()))
