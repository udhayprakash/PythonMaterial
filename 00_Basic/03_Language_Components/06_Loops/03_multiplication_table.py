#!/usr/bin/python

MIN = 0
MAX = 12

a = MIN
while a < MAX:
    a += 1
    b = MIN
    while b < MAX:
        b += 1
        #print a, '*', b, '=', a * b, '|'
        print '| %2d * %2d = %3d  |'%(a, b, a * b)
    print '-'*20
