#!/usr/bin/python
"""
Purpose: Boolean Operations
"""

# True, False

choice = True
print 'choice = ', choice

true = 'Udhay Prakash'  # NOT RECOMMENDED to use 'true' for variable name

choice = true
print 'choice = ', choice

choice = False
print 'choice = ', choice

# Object 
#  - address location where it is stored - id()
#  - type(s)
#  - value(s)

print "id(True) = ", id(True)
print "id(true) = ", id(true)

print "type(True) =", type(True)
print "type(true) =", type(true)

print "True = ", True
print "True * 30 = ", True * 30   # True has a value of one

print "False = ", False
print "False * 30 = ", False * 30   # False has a value of zero


print "True == 1 ", True == 1
print "True == 3 ", True == 3
print "True != 3 ", True != 3


print "False == 0 ", False == 0
print "False == 3 ", False == 3
print "False != 3 ", False != 3



## bool()
# integer type (int, long and float)
#       zero     - False 
#       non-zero - True
print "bool(12)", bool(12)
print "bool(-12)", bool(-12)
print "bool(0)", bool(0)

print "bool(0.00)", bool(0.00)
print "bool(0.000000001)", bool(0.000000001)
print "bool(-0.000000001)", bool(-0.000000001)


# strings
#  True - non-empty string 
#  False - empty string
print "true", true
print "bool(true)", bool(true)
print "bool('')", bool('')

# [], (), {}