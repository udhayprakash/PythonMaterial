#!/usr/bin/python
"""
initialization
while loop- condition
    increment/decrement
    logic
"""

MIN = 0
MAX = 12

a = MIN  # initialization
while a < MAX:  # condition
    a += 1  # increment
    b = MIN
    while b < MAX:
        b += 1
        # print a,  '*', b, '=', a*b
        # print "%d * %d = %d" % (a, b, a * b)
        # print "%2d * %2d = %3d" % (a, b, a * b)
        print "{} * {} = {}".format(a, b, a*b)
    print '-' * 18, a
    # break
else:
    print 'All iterations in while loop completed'

print 'next statement'
