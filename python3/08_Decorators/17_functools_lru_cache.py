#!/usr/bin/python
"""
Purpose: Least Recently Used (LRU) Cache
    - cache is a place that is quick to access where
    you store things that are otherwise slow to access.
    - cache can only ever store a finite amount of things,
    and often is much smaller than whatever it is caching.
    - cache performs really well when it contains the
    thing you are trying to access, and not so well when
    it doesn't.
    - The percentage of times that the cache contains the
    item you are looking for is called the hit rate.
    - The primary factor in hit rate (apart from cache size)
    is replacement strategy.
    - Under the hood, an LRU cache is often implemented by
    pairing a doubly linked list with a hash map.

Strengths:
    1. Super fast accesses.
        - LRU caches store items in order from
          most-recently used to least-recently used.
        - That means both can be accessed in O(1) time.
    2. Super fast updates.
        - Each time an item is accessed, updating the
        cache takes O(1) time.

Weaknesses
    1. Space heavy.
        - An LRU cache tracking nn items requires
        a linked list of length nn, and a hash map
        holding nn items.
        - That's O(n) space, but it's still two
        data structures (as opposed to one).
"""
import functools

@functools.lru_cache(maxsize=4)
def fibonacci(num):
    print(f'Calculating fibonacci({num})')
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


if __name__ =='__main__':
    fibonacci(2)
    print()

    fibonacci(4)
    print()

    fibonacci(8)
    print()

    print(f'\n{fibonacci.cache_info() =}')
