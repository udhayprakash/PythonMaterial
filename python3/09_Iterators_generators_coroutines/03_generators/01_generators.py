#!/usr/bin/python
"""
Purpose: Generators
"""


def my_generator():
    print(' I am in the function')
    # return 111
    print('yielding 222')
    yield 222
    print('yielding 333')
    yield 333
    print('yielding 444')
    yield 444
    print('yielding 555')
    yield 555


m = my_generator()
print(m)

print(next(m))     # 222
print('outside')
print(next(m))     # 333
print('outside')
print(next(m))     # 444
print('outside')
print(next(m))
print('outside')

try:
    print(next(m))
except StopIteration as ex:
    print(repr(ex))