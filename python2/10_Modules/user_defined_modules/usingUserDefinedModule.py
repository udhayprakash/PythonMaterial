#!/usr/bin/python

"""
Purpose: Usage of user-defined module
"""

import myFile1

print dir(myFile1)

# print myFile1.__builtins__

print myFile1.__doc__

print '-' * 80

print help(myFile1)

print '-' * 80
print 'addition result = ', myFile1.addition(10, 20)

print 'addition =', myFile1.addition(myFile1.num1, myFile1.num2)

print myFile1.addition.__doc__


# reload()  - generally useful in interactive mode to reload the module
#             Useful when changes needed to be updated during execution
