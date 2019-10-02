#!/usr/bin/python

class OrdinaryCClass:
    def __init__(self):
        self.foo = None
        self.bar = None


o = OrdinaryCClass()
# print('o.foo', o.foo)

# Dynamically creating attributes
o.xxx = 12312  # adhoc attribites can be added to instance
setattr(o, 'yy', 999)

print(vars(o))
print()


class SlottedClass:
    """
    when __slots__ is present, it wont allow 
    to create dynamic attributes
    """
    __slots__ = ('foo', 'bar')

    def __init__(self):
        self.foo = None
        self.bar = None


c = SlottedClass()
# print(dir(c))
print(f'c.foo={c.foo}')
c.foo = 123
print(f'c.foo={c.foo}')

# can't create new attribute 
try:
    c.xxx = 12312  # adhoc attribites can be added to instance
    setattr(c, 'yy', 999)
except AttributeError as ex1:
    print(repr(ex1))

# c.xxx = 123          # adhoc attribites CANT be added to instance
