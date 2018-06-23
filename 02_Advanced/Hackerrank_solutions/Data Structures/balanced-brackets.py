#!/bin/python
"""
https://www.hackerrank.com/challenges/balanced-brackets/problem
"""
import sys

def isBalanced(s):
    stack = []
    for ch in s:
        if ch == ')':
            stack.remove('(')
        elif ch == ']':
            stack.remove('[')
        elif ch == '}':
            stack.remove('{')
        else:
            stack.append(ch)
    print 'stack:', stack
    return 'YES' if not stack else 'NO'

if __name__ == "__main__":
    t = int(raw_input().strip())
    if 1 <= t <= 10**3:
        for a0 in xrange(t):
            s = raw_input().strip()
            if 1 <= len(s) <= 10**3:
                result = isBalanced(s)
                print result

