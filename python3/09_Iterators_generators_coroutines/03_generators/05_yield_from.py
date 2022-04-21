#!/usr/bin/python3
"""
Purpose: Usage of yield from
        - can be used with any iterable object
"""


def num_generator(n):
    for i in range(n):
        yield i


ng = num_generator(10)
print(f'{list(ng) = }')


def sequence_parser(mylist):
    for ele in mylist:
        yield ele


sp = sequence_parser([12, 34, 56, 78, 90])
print(f'{tuple(sp) =}')
print()


# Method 2 - using "yield from"
def num_generator(n):
    # for i in range(n):
    #     yield i
    yield from range(n)


ng = num_generator(10)
print(f'{list(ng) = }')


def sequence_parser(mylist):
    # for ele in mylist:
    #     yield ele
    yield from mylist


sp = sequence_parser([12, 34, 56, 78, 90])
print(f'{tuple(sp) =}')
