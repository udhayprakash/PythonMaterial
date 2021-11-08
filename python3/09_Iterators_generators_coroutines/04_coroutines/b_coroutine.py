#!/usr/bin/python3
"""
Purpose: Coroutines
"""


def my_coroutine(num):
    value = yield "default string"
    yield value
    yield value
    value = yield "new string"
    yield value


# Step 1: To call
c = my_coroutine(4)
print(f'{type(c)    = }')  # <class 'generator'>
print(f'{c          = }')  # <generator object my_coroutine at 0x0000022D8B349A10>

# Step 2: to prime the generator to become coroutine
print(f'{next(c) =}')  # 'default string'

# Step 3: Sending values to coroutine
print(f"{c.send('first')  =}")  # 'first'
print(f"{c.send('second') =}")  # 'first'
print(f"{c.send('third')  =}")  # 'new string'

# To close the coroutine
c.close()
