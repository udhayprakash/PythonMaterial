#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Purpose: Coroutines
    - pep-0342
    - generators are data producers
    - coroutines are data consumers

    - Coroutines consume values using a (yield)

"""


def hello():  # -- generator
    # print('Hello world')
    # return 'Hello world'
    yield 'Hello world'


result = hello()
print(f'{type(result)} {result}')  # generator
print(f'{next(result) = }')  # 'Hello world'


# ------------------------------
def hello():  # coroutine
    value = yield 'Hello world'
    yield value


result = hello()
print(f'{type(result)} {result}')  # generator
print(f'{next(result) = }')  # 'Hello world'


# ------------------------------
def hello():  # coroutine
    value = yield
    yield value


# NOTE: Default initial yield is None

result = hello()
print(f'{type(result)} {result}')
print(f'{next(result) = }')  # None
print()


# ------------------------------
def hello():  # coroutine
    value = yield 123123
    # yield value
    yield f'Passed value is {value}'


result = hello()
print(f'{type(result)} {result}')

# All coroutines must be "primed" by first calling next() (or send(None))
print(f'{next(result) = }')

print(f'{result.send("world") = }')   # 'Passed value is world'


try:
    print(f"{result.send('Python')  =}")
except StopIteration:
    print('No more yields to send !!!')
