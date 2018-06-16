#!/usr/bin/python
"""
Purpose: python syntax and basics
"""
name = "Almighty"

print name 

print "Name of the student:", name
# , (comma) logic separator operator
print "Name of the student:"+ name

name = 123
print "Name of the student:", name
# , (comma) logic separator operator
# print "Name of the student:"+ name # TypeError: cannot concatenate 'str' and 'int' objects


# no difference between single and double quotes
# for strings 

print 'Hello'
print 'world'

print 'Hello',  
print 'world'

# if ,(comma) is present at the end of print statement, 
# it acts as a new line suppressor operator

print 'Hello', 'udhay',
print 'world'
