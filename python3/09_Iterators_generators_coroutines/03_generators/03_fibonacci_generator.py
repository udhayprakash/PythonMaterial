#!/usr/bin/python3
"""
Purpose: Fibonacci Series
    - first two values are 0 & 1
    - subseqeunt values are summation of previous two values
    - 0, 1, 1, 2, 3, 5, 8, 13, ...
"""


# Method 1 -- using functions -- you get all values at a time
def fib_series(num):
    if num < 0:
        return "Invalid Input"
    fib_nums = []
    a, b = 0, 1
    for _ in range(0, num):
        fib_nums.append(a)
        a, b = b, a + b
    return fib_nums


result = fib_series(10)
print(result)


# Method 2 -- using Generators
def fib_series(num):
    if num < 0:
        yield "Invalid Input"
    a, b = 0, 1
    for _ in range(0, num):
        yield a
        a, b = b, a + b


result = fib_series(10)
print(result)

for each_fib in fib_series(10):
    print(each_fib)

print()
print(list(fib_series(15)))

print()
print(tuple(fib_series(-3)))
print()


# Method 2b - using generators
def fib_series2(num):
    yield 1
    yield 1
    curr, prev = 2, 1
    while curr < num:
        yield curr
        curr, prev = curr + prev, curr


print(list(fib_series2(10)))  # [1, 1, 2, 3, 5, 8]
