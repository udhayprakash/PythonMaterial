#!/usr/bin/python3
"""
Purpose: Least Recently Used (LRU) Cache

    lru_cache(maxsize, typed)
    - maxsize: how many results of this function call can be cached 
               at most, if None, there is no limit, when set to a 
               power of 2, the performance is the best
    - typed: If True, calls of different parameter types will be
              cached separately.
"""
import timeit
from functools import lru_cache


@lru_cache(None)
def add(x, y):
    print(f'calculating: {x} + {y}')
    return x + y


print(add(1, 2))
print(add(1, 2))  # call is not made
print(add(1, 3))


# ----------------------
# Case 1
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n - 1)


print(timeit.timeit(lambda: fib(40), number=1))  # 32.758174600000004

# ----------------------
# Case 2


@lru_cache(None)
def fib2(n):
    if n < 2:
        return n
    return fib2(n-2) + fib2(n - 1)


print(timeit.timeit(lambda: fib(40), number=1))  # 2.2999999998774e-05


# ----------------------
@lru_cache(maxsize=100)
def count_vowels(sentence):
    sentence = sentence.casefold()
    return sum(sentence.count(vowel) for vowel in 'aeiou')


print(count_vowels("Welcome to Python"))
