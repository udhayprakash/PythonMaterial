#!/usr/bin/python
"""
Purpose: Data classes
  Introduced in python 3.7 (with PEP 557) to reduce the boilerplate code
  For 3.6, dataclasses can be used by installing as a module
                pip install dataclasses

"""
from dataclasses import dataclass


@dataclass()
class Foo(object):
    x: int


f = Foo(12)
print(f'{f.x =}')
f.x = 1
f.y = 12        # Adding new attrbute to instance

try:
    print(hash(f))
except Exception as ex:
    print(ex)
    print('This instance is mutable. So, hash cant be created')

print('\nWith FROZEN =============')


@dataclass(frozen=True)
class Foo(object):
    x: int


f = Foo(12)
print(f'{f.x =}')
# f.x = 1 # dataclasses.FrozenInstanceError: cannot assign to field 'x'
# f.y = 123 # dataclasses.FrozenInstanceError: cannot assign to field 'y'
print(hash(f))

# NOTE: Namedtuples are also dataclasses,
# but immutable by default
