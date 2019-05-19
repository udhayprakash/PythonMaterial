#!/usr/bin/python
"""
Purpose: Boolean Operations
"""
## bool()
# integer type (int and float)
#       zero     - False 
#       non-zero - True
print("bool(12)          ", bool(12))
print("bool(-12)         ", bool(-12))
print("bool(0)           ", bool(0))
print()
print("bool(0.00)        ", bool(0.00))
print("bool(0.000000001) ", bool(0.000000001))
print("bool(-0.000000001)", bool(-0.000000001))
print()

# strings
#  True - non-empty string 
#  False - empty string
print("bool('ball')     ", bool('ball'))
print("bool(' ')        ", bool(' '))  # white-space
print("bool('')         ", bool(''))  # empty string
print()

# braces
# [], (), {}
print('(1)              ', bool((1)))
print('(1,)             ', bool((1,)))
print('[1]              ', bool([1]))
print('{1}              ', bool({1}))
print('{1:2}            ', bool({1: 2}))
print()

print('()               ', bool(()))
print('[]               ', bool([]))
print('{}               ', bool({}))

# True, False
print('bool(True)       ', bool(True))
print('bool(False)      ', bool(False))
print()
##########################

print('bool(9>34)', bool(9>34))  # bool(False) => False
