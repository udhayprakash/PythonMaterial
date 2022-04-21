#!/usr/bin/python3
"""
Purpose: Generators
"""

def simple_gen():
    yield 'Hello'
    yield 'world'

gen = simple_gen()
print(f'{gen            = }')
print(f'{next(gen)      = }')
print(f'{gen.__next__() = }')
print()

# ------------------------------
def countDown(n):
    print('YOur count Down starts now!')
    i = 0
    while i < n:
        print(f'yielding {i}')
        yield i
        i += 1
    print('CountDOWN completed')
    return 'NO more values'


# PEP8 strongly discourages usage of yield and
# retun, in same function

c = countDown(10)
print(f'{c              = }')
print(f'{next(c)        = }')


for val in c:
    print(f'{val = }')

# print(f"{c.__next__()   = }")
