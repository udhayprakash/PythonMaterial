#!/usr/bin/python
"""
Purpose: __slots__ importance
"""


import sys

from pympler.asizeof import asizeof


class OrdinaryClass:
    """
    Generally, all class instances are mutable
    """

    def __init__(self):
        self.foo = None
        self.bar = None


o = OrdinaryClass()
print(vars(o))

# Dynamically creating attributes
o.xxx = 12312  # adhoc attributes can be added to instance
setattr(o, "yy", 999)

print(vars(o))
print()

# ---------------------------------------------


class SlottedClass:
    """
    when __slots__ is present, it wont allow
    to create dynamic attributes
    """

    __slots__ = ("foo", "bar")

    def __init__(self):
        self.foo = None
        self.bar = None
        # self.something = None
        # # AttributeError: 'SlottedClass' object has no attribute 'something'


print()
c = SlottedClass()
# print(vars(c))
# TypeError: vars() argument must have __dict__ attribute


# updating existing attribute values are possible
print(f"c.foo={c.foo}")
c.foo = 123
print(f"c.foo={c.foo}")


# can't create new attribute
try:
    c.xxx = 12312  # adhoc attributes can be added to instance
    setattr(c, "yy", 999)
except AttributeError as ex1:
    print(repr(ex1))


print(f"{sys.getsizeof(o) =}")
print(f"{sys.getsizeof(c) =}")

# pympler.asizeof can be used to investigate how much memory
# certain Python objects consume. In contrast to sys.getsizeof,
# asizeof sizes objects recursively.

print(f"{asizeof(o) =}")
print(f"{asizeof(c) =}")

# -------------------------
class A:
    __slots__ = ["x", "y", "z"]
    w = 1


class B(A):
    __slots__ = ["w", "z"]
    pass


a = A()
b = B()
