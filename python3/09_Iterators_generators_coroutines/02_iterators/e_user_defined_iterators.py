#!/usr/bin/python
"""
Purpose:
"""

a = ['foo', 'bar', 'baz']

itr = iter(a)
print(itr)

print('itr.__next__()', itr.__next__())
print('next(itr)     ', next(itr))
print('next(itr)     ', next(itr))

try:
    print('next(itr)     ', next(itr))
except StopIteration as ex:
    print(repr(ex))