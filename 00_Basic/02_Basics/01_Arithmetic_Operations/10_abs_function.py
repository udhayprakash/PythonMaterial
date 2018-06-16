#!/usr/bin/python
"""
Builtin function, to return the absolute value.

If a is positive real integer, 
    abs(a)  = a
    abs(-a) = a
    abs((a+bj))  is equal to math.sqrt(pow(a,2), pow(b,2))
"""

print "abs(3)          = ", abs(3)
print "abs(-3)         = ", abs(-3)
print "abs(0.00000001) = ", abs(0.00000001)
print "abs(-3 + 4j)    = ", abs(-3 + 4j)    # 5.0
print "abs(-3 + 4.0j)  = ", abs(-3 + 4.0j)  # 5.0

# loaing a module (library) to use
import math

print math.sqrt(pow(-3, 2) + pow(4, 2))    # 5.0
print math.sqrt((-3) ** 2 + 4 ** 2)        # 5.0

print math.sqrt(-3 ** 2 + 4 ** 2)          # 2.64575131106- PEMDAS
