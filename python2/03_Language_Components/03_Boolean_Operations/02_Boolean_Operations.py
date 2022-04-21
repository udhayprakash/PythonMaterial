#!/usr/bin/python
"""
Purpose: Boolean Operations
"""

# True, False


print 'True == 1 ', True == 1
print 'True == 3 ', True == 3
print 'True != 3 ', True != 3

print 'False == 0 ', False == 0
print 'False == 3 ', False == 3
print 'False != 3 ', False != 3

# True acts like  1 and
# False acts like 0 in all cases, except when coverted
# to strings
print 'str(1) != str(True)', str(1) != str(True)
print 'str(0) != str(False)', str(0) != str(False)

print str(1)
print str(True)
'''
    >>> str(1)
    '1'
    >>> str('True')
    'True'
    >>> str(0)
    '0'
    >>> str(False)
    'False'
    >>>
'''
