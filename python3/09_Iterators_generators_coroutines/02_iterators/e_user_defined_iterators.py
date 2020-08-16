#!/usr/bin/python
"""
Purpose: Iterators
            - To get values from an iterator objects 
                1. Iterate over it 
                        - for loop 
                        - converting to other iterables 
                            - list(), tuple(), set(), dict()
                2. To apply next()
                    - will result in one element at a time
"""

a = ['foo', 'bar', 'baz']

itr = iter(a)
print(itr)    # <list_iterator object at 0x0000028542B600A0>


print('itr.__next__()', itr.__next__())
print('next(itr)     ', next(itr))
print('next(itr)     ', next(itr))

try:
    print('next(itr)     ', next(itr))
except StopIteration as ex:
    print(repr(ex))


print('\nReassigning')
itr = iter(a)
while True:
    try:
        print('next(itr)     ', next(itr))
    except StopIteration as ex:
        print(repr(ex))
        break
