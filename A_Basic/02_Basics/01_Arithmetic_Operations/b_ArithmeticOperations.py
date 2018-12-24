#!/usr/bin/python

"""
Purpose: Demonstration of Arithmetic Operations


Integer family 
    int 
    long 
    float 

    complex
    bool
"""

# + - * / // %
# NOTE: PEP 8 recommends to place one space around the operator
print 'Modulo Operation  % - remainder'

print '13 % 2=', 13 % 2

print '-13 % 2=', -13 % 2
print '13 % -2=', 13 % -2
print '-13 % -2=', -13 % -2

print
print 'power operation **'

print '4 ** 2 = ', 4 ** 2
print '64 ** (1/2) = ', 64 ** (1 / 2)  # square root
print '64 ** (1/2.0) = ', 64 ** (1 / 2.0)  # square root
print '64 ** 0.5 = ', 64 ** 0.5  # square root

print 'pow(4,2)   =', pow(4, 2)
print 'pow(64,1/2)=', pow(64, 1 / 2)
print 'pow(64,0.5)=', pow(64, 0.5)
print
print 'pow(4,2,9) =', pow(4, 2, 9) # (4 ** 2) % 9

print
print 'Exponent Notation'
print '1e1 = ', 1e1

print '1 * 10.0 ** 1 = ', 1 * 10.0 ** 1

print '3e2 =', 3e2  # 3 * 10.0 ** 2
print '-2.3e4 = ', -2.3e4  # -2.3 * 10.0 ** 4
