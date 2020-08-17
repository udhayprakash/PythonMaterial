#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Purpose: Coroutines
    - pep-0342
    - generators are data producers
    - coroutines are data consumers

    - Coroutines consume values using a (yield)

valid syntax:
    x = yield 42
    x = yield
    x = 12 + (yield 42)
    x = 12 + (yield)
    foo(yield 42)
    foo(yield)

invalid syntax:
    x = 12 + yield 42
    x = 12 + yield
    foo(yield 42, 12)
    foo(yield, 12)
"""


def hello():
    # print('Hello world')
    # return 'Hello world'
    # yield 'Hello world'
    value = yield
    yield value


result = hello()
print(f'{result =}')

print(f'{next(result) =}')


# ---------------------------
print()


def hello1():
    value = yield 123232
    # yield value
    yield f'Passed value is {value}'


# NOTE: Default initial yield is None
result1 = hello1()

# All coroutines must be "primed" by first calling .next() (or send(None))
print(f'{next(result1) =}')

print(f"{result1.send('World!')  =}")


try:
    print(f"{result1.send('Python')  =}")
except StopIteration:
    print('No more yields to send !!!')
