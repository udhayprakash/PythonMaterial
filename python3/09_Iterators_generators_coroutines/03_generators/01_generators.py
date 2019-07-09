#!/usr/bin/python
"""
Purpose: Generators
"""


def my_generator():
    print(' I am in the function')
    # return 1
    print('yielding 1')
    yield 1
    print('yielding 2')
    yield 2
    print('yielding 3')
    yield 3
    print('yielding 4')
    yield 4
    

m = my_generator()
print(m)

print(next(m))
print('outside')
print(next(m))
print('outside')
print(next(m))
print('outside')
print(next(m))
print('outside')

try:
    print(next(m))
except StopIteration as ex:
    print(repr(ex))