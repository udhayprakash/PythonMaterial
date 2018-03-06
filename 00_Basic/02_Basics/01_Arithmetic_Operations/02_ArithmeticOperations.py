#!/usr/bin/python
"""
Purpose: Demonstration of Arithmetic Operations
"""

# compound operators
#  += -= *= /= %=

myNumber = 123
print 'myNumber = ', myNumber

myNumber = myNumber + 1
print 'myNumber = ', myNumber

# In cases, where the same variable is present both the sides, then compound operations are valid

myNumber += 1   # myNumber = myNumber + 1
print 'myNumber = ', myNumber

myNumber -= 58   # myNumber = myNumber - 58
print 'myNumber = ', myNumber

myNumber *= 100   # myNumber = myNumber * 100
print 'myNumber = ', myNumber

myNumber /= 10   # myNumber = myNumber / 10
print 'myNumber = ', myNumber

myNumber %= 10   # myNumber = myNumber % 10
print 'myNumber = ', myNumber

print '-----------------------------------------------'
print 'bitwise Operations'
# >> <<
myNewNumber = 4
print 'myNewNumber =', myNewNumber

result = myNewNumber << 1
print 'result = ', result

#    8 4 2 1
#4-  0 1 0 0
#<<  1 0 0 0

result = 14 >> 2
print "14 >> 2 = ", result
#    8 4 2 1
#14  1 1 1 0
>>2  0 0 1 1
