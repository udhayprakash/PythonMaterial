#!/usr/bin/python
"""
Purpose: To make a Fibonacci generator: 0, 1, 1, 2, 3, 5, ...
"""


def fibonacci(max):
    """
    fibonacci function
    """
    n, a, b = 0, 0, 1
    while n < max:
        yield a
        a, b = b, a + b
        n = n + 1


print '__name__', __name__

if __name__ == '__main__':  # This condition gets executed, only if the python script is directly executed
    fib10 = fibonacci(10)
    for i in fib10:
        print i,
