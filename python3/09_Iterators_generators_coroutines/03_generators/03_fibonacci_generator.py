#!/usr/bin/python3
"""
Purpose: Fibonacci Series 
    - first two values are 0 & 1
    - subseqeunt values are summation of previous two values
    - 0, 1, 1, 2, 3, 5, 8, 13, ...
"""
# Method 1


def fib_series(num):
    a, b = 0, 1
    if num < 0:
        yield 'Invalid input'
    else:
        for i in range(0, num):
            yield "{}:{:3}".format(i, a)
            a, b = b, a + b


result = fib_series(10)
print(result)

for each_fib in fib_series(10):
    print(each_fib)

print()
print(list(fib_series(15)))

print()
print(tuple(fib_series(-3)))



# Method 2
print()
def fib_series2(num):
    yield 1
    yield 1
    curr = 2
    prev = 1
    while curr < num:
        yield curr
        curr, prev = curr + prev, curr
print(list(fib_series2(10)))
