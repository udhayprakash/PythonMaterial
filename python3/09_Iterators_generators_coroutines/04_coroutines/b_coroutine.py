#!/usr/bin/python3
"""
Purpose: Coroutines
"""
def my_coroutine(num):
    value = yield "default string"
    yield value
    yield value
    yield value


# Step 1: Tocall 
c = my_coroutine(4)
print(f'{type(c)    = }')  # <class 'generator'>
print(f'{c          = }')  # <generator object my_coroutine at 0x000001F2C8DC8200>


# Step 2: to prime the generator to become coroutine
print(f'{next(c) =}')


# Step 3: Sending values to coroutine 
print(f"{c.send('first')  =}")
print(f"{c.send('second') =}")
print(f"{c.send('third')  =}")


# To close the coroutine
c.close()