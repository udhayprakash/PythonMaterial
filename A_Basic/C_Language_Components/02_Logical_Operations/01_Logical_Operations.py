#!/usr/bin/python
"""
Purpose: Logical Operations


and - if  all are True, result is True 
or  - if any one of them is True, result is True
not - negate the existing value 
"""

# and,  or,  not  

expr1 = (12 > 34) and (99 >= 9)
#        False          True
print expr1

'''
and
---
True and True = True

'''
print 'and operation '
print "True and True  ", True and True
print "True and False ", True and False
print "False and True  ", False and True
print "False and False ", False and False

print
print 'or operation '
print "True or True  ", True or True
print "True or False ", True or False
print "False or True  ", False or True
print "False or False ", False or False
print
print "True     ", True
print "not True ", not True
print "not False ", not False

print '============================='

expr2 = (45 <= 45) or (3 > 333)
#       True          False
print expr2

expr2 = (45 <= 45) or (3 > 333) and (9 == 9)
#       True          False         True
print expr2

# left to right and top to bottom


expr3 = 0 and 1
print 'expr3=', expr3

expr4 = 3 and 9
print 'expr4=', expr4
