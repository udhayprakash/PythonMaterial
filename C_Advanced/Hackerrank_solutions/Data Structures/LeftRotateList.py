#!/bin/python

import sys

def leftRotation(a, d):
    if 1 <= n <= 10**5 and 1 <= d <= n:
        if all(map(lambda x: 1 <= x <= 10**6, a)):
            return a[d:]+ a[:d]
            

if __name__ == "__main__":
    n, d = raw_input().strip().split(' ')
    n, d = [int(n), int(d)]
    a = map(int, raw_input().strip().split(' '))
    result = leftRotation(a, d)
    print " ".join(map(str, result))


