#!/usr/bin/python
"""
Purpose: 
https://www.hackerrank.com/challenges/mark-and-toys/problem?isFullScreen=true
"""


def maximumToys(prices, k):
    prices.sort()
    for _index, ech in enumerate(prices, start=1):
        k -= ech
        if k < 0:
            break
    return _index - 1


assert maximumToys([1, 2, 3, 4], 7) == 3
assert maximumToys([3, 7, 2, 9, 4], 15) == 3
assert maximumToys([1, 12, 5, 111, 200, 1000, 10], 50) == 4
assert maximumToys([45], 50) == 1
assert maximumToys([45, 5], 50) == 2
assert maximumToys([45, 6], 50) == 1
