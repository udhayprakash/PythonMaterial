#!/usr/bin/python
"""
Purpose: range() and xrange()
"""

values = range(9)  # builtin function
print values
print 'type(values):', type(values)

# collections - List, tuple, set, dictionary

values1 = range(0,9)  # builtin function
print values1

values2 = range(0,9,1)  # builtin function
print values2

# range(initialValue, finalValue, step)
# default initialValue = 0
# default step = +1

values3 = range(9,0, -1)  # builtin function
print values3

values4 = range(9,0, -2)  # builtin function
print values4

print '-'*80
values = xrange(9)  # builtin function
print values
print 'type(values):', type(values)

# collections - List, tuple, set, dictionary

values1 = xrange(0,9)  # builtin function
print values1

values2 = xrange(0,9,1)  # builtin function
print values2

# range(initialValue, finalValue, step)
# default initialValue = 0
# default step = +1

values3 = xrange(9,0, -1)  # builtin function
print values3

values4 = xrange(9,0, -2)  # builtin function
print values4

print '-'*80

for i in range(9):
    print i,       # , acts as a new-line suppressor

print

for i in xrange(9):
    print i,        # , acts as a new-line suppressor

print

for ch in 'Python Programming':
    print ch,

# for loop can be applied on iterable object (string, list, tuple, set, frozenset, dictionary) only
