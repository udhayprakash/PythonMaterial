#!/usr/bin/python
"""
Purpose: __slots__ importance
"""


class OrdinaryCClass:
    """
    Generally, all class instances are mutable
    """

    def __init__(self):
        self.foo = None
        self.bar = None


o = OrdinaryCClass()
print(vars(o))

# Dynamically creating attributes
o.xxx = 12312  # adhoc attributes can be added to instance
setattr(o, 'yy', 999)

print(vars(o))
print()


# ---------------------------------------------
class SlottedClass:
    """
    when __slots__ is present, it wont allow
    to create dynamic attributes
    """
    __slots__ = ('foo', 'bar')

    def __init__(self):
        self.foo = None
        self.bar = None
        # self.something = None
        # # AttributeError: 'SlottedClass' object has no attribute 'something'


c = SlottedClass()
# print(vars(c))

# updating existing attribute values are possible
print(f'c.foo={c.foo}')
c.foo = 123
print(f'c.foo={c.foo}')

# can't add new attribute

# can't create new attribute
try:
    c.xxx = 12312  # adhoc attributes can be added to instance
    setattr(c, 'yy', 999)
except AttributeError as ex1:
    print(repr(ex1))


