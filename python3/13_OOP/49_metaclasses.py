#!/usr/bin/python3
"""
Purpose: Metaclasses
    - Used for creating classes dynamically
    - useful for code injections
"""
from pprint import pprint

# Method 1: creating class & instance ordinarily


class NewType(object):
    x = 'hello'


n2 = NewType()
print(f'{n2.x =}')  # 'hello'


# Method 2: Creating class & instance using metaclasses
NewType = type('NewType', (object,), {'x': 'hello'})
n1 = NewType()
print(f'{n1.x =}')  # 'hello'


print(f'{n1 = } {id(n1) =}')
print(f'{n2 = } {id(n2) =}')

print('\n\n Anonymous types')

MyClass = type('', (object,), {'x': 'blah'})
print(f'{MyClass =}')  # <class '__main__.'>

my_inst = MyClass()
print(f'{my_inst.x =}')
print('\n\n')
# -----------------------------------------
print(f'{type                  =}')
print(f'{type.__bases__        =}')
print()

descriptor = type.__dict__['__bases__']
print(f'{descriptor            =}')
print(f'{type(descriptor)      =}')
print()

class MyMeta(type):
    @property        # a property is a descriptor
    def foo(cls):
        return 'foo'


class MyClass(metaclass=MyMeta):
    pass


pprint(vars(MyClass))
print('MyClass.foo:', MyClass.foo)
