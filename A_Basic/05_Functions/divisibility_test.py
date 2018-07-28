#!/usr/bin/python
"""
Purpose: Divisibility test
"""


def divisibility_test(m, n):
    if m % n == 0:
        print "%2d is divisible by     %2d" % (m, n)
    else:
        print "%2d is not divisible by %2d" % (m, n)


divisibility_test(6, 9)
divisibility_test(6.0, 6)
divisibility_test(-6, 9.0)
divisibility_test(-6, -6)













