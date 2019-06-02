#!/usr/bin/python

class OrdinaryCClass:
    def __init__(self):
        self.foo = None 
        self.bar = None 
        
o = OrdinaryCClass()
print(dir(o)), 
print('o.foo', o.foo)

o.xxx = 12312          # adhoc attribites can be added to instance

print()

class SlottedClass:
    __slots__ = ('foo', 'bar')

c = SlottedClass()

print(dir(c))
# print('c.foo', c.foo)

c.foo = 32
print('c.foo', c.foo)

c.xxx = 123          # adhoc attribites CANT be added to instance