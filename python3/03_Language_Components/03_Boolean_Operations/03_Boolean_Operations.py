#!/usr/bin/python
"""
Purpose: Boolean Operations
"""
## bool()
# integer type (int and float)
#       zero     - False 
#       non-zero - True
print("bool(12)", bool(12))
print("bool(-12)", bool(-12))
print("bool(0)", bool(0))
print()
print("bool(0.00)", bool(0.00))
print("bool(0.000000001)", bool(0.000000001))
print("bool(-0.000000001)", bool(-0.000000001))
print()
# strings
#  True - non-empty string 
#  False - empty string
true = 'Udhay Prakash'  # NOT RECOMMENDED to use 'true' for variable name
print("true", true)
print("bool(true)", bool(true))
print("bool('ball')", bool('ball'))
print("bool('')", bool(''))  # empty string
print("bool(' ')", bool(' '))  # white-space
print()
# [], (), {}
print('(1)', bool((1)))
print('(1,)', bool((1,)))
print('[1]', bool([1]))
print('{1}', bool({1}))
print('{1:2}', bool({1: 2}))
print()
print('()', bool(()))
print('[]', bool([]))
print('{}', bool({}))

# True, False
print('bool(True)', bool(True))
print('bool(False)', bool(False))
##########################
print()
print('bool(9>34)', bool(9>34))  # bool(False) => False

if not 0:
    print("hello")

while 1:
    print("hello")
    break 

num1 = -0.000000056
if num1:
    print("a=", num1)


if num1 >= 9:
    print("a=", num1)


# bool( num1>=9)
# bool(False)
# False

if not num1>=9:
    print("a=", num1)

