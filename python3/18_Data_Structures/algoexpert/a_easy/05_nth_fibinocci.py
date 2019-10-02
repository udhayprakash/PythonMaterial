#!/usr/bin/python
"""
Purpose: 
The Fibonacci sequence is defined as follows: 
    the first number of the sequence is 0, the secondsond number is 1, 
    and the nth number is the sum of the (n - 1)th and (n - 2)th numbers. 
Write a function that takes in an integer n and returns the nth Fibonacci number.

sample input: 6 
sample output : 5 (0, 1, 1, 2, 3, 5)
"""
from time import perf_counter


def getNthFib(n):
    """
    Recursion Based Solution
    F(n) = F(n-1) + F(n-2) for n > 2

    Time Complexity : O(2 ^ n)
    Space Complexity: O(n)
    """
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return getNthFib(n - 1) + getNthFib(n - 2)


start_time = perf_counter()
print(f'\ngetNthFib(6)  :{getNthFib(6)}')
print(f'time taken    :{perf_counter() - start_time: 8} seconds')


# start_time= perf_counter()   ==========> FAILS
# print(f'getNthFib(100):{getNthFib(100)}')
# print(f'time taken    :{perf_counter() - start_time: 8} seconds')

def getNthFib(n, memoize={1: 0, 2: 1}):
    """
    Time Complexity : O(n)
    Space Complexity: O(n)
    """
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFib(n - 1, memoize) + getNthFib(n - 2, memoize)
        return memoize[n]


start_time = perf_counter()
print(f'\ngetNthFib(6)  :{getNthFib(6)}')
print(f'time taken    :{perf_counter() - start_time: 8} seconds')

start_time = perf_counter()
print(f'getNthFib(100):{getNthFib(100)}')
print(f'time taken    :{perf_counter() - start_time: 8} seconds')


def getNthFib(n):
    """
    Time Complexity : O(n)
    Space Complexity: O(1)
    """
    last_two = [0, 1]
    counter = 3
    while counter <= n:
        next_fib = last_two[0] + last_two[1]
        last_two[0] = last_two[1]
        last_two[1] = next_fib
        counter += 1
    return last_two[1] if n > 1 else last_two[0]


start_time = perf_counter()
print(f'\ngetNthFib(6)  :{getNthFib(6)}')
print(f'time taken    :{perf_counter() - start_time: 8} seconds')

start_time = perf_counter()
print(f'getNthFib(100):{getNthFib(100)}')
print(f'time taken    :{perf_counter() - start_time: 8} seconds')


def getNthFib(n):
    """
    Time Complexity : O(n-2)
    Space Complexity: O(1)
    """
    # memoization design pattern
    a, b = 0, 1
    for _ in range(n - 1):  # range ignores 1, so, -1
        a, b = b, a + b
    return a  # nth value 


start_time = perf_counter()
print(f'\ngetNthFib(6)  :{getNthFib(6)}')
print(f'time taken    :{perf_counter() - start_time: 8} seconds')

start_time = perf_counter()
print(f'getNthFib(100):{getNthFib(100)}')
print(f'time taken    :{perf_counter() - start_time: 8} seconds')

# assert getNthFib(6) == 5
# assert getNthFib(1) == 0
# assert getNthFib(2) == 1
# assert getNthFib(3) == 1
# assert getNthFib(4) == 2
# assert getNthFib(5) == 3
# assert getNthFib(6) == 5
# assert getNthFib(7) == 8
# assert getNthFib(8) == 13
# assert getNthFib(9) == 21
# assert getNthFib(10) == 34
# assert getNthFib(11) == 55
# assert getNthFib(12) == 89
# assert getNthFib(13) == 144
# assert getNthFib(14) == 233
# assert getNthFib(15) == 377
# assert getNthFib(16) == 610
# assert getNthFib(17) == 987
# assert getNthFib(18) == 1597
