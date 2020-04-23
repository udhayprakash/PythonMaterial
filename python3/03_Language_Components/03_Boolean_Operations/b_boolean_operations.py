#!/usr/bin/python
"""
Purpose: Boolean Operations
"""


# == value level equivalence
print("True == 1  ", True == 1)
print("True == 3  ", True == 3)
print("True != 3  ", True != 3)

print("False == 0 ", False == 0)
print("False == 3 ", False == 3)
print("False != 3 ", False != 3)

print()
print("True == 1.0  ", True == 1.0)
print("False == 0.0  ", False == 0.0)

print()
# True acts like  1 and False acts like 0 in all cases,
# except when converted to strings
print("str(1) != str(True) ", str(1) != str(True))
print("str(0) != str(False)", str(0) != str(False))

print()
print('str(True * 1) == str(1)', str(True * 1) == str(1))
print(str(1))
print(str(True))

'''
    >>> str(1)
    '1'
    >>> str(True)
    'True'
    >>> str(0)
    '0'
    >>> str(False)
    'False'
    >>> str(True * 1)
	'1'
'''
