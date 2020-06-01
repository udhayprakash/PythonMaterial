#!/usr/bin/python
"""
Purpose: String Attributes
"""
print("42".zfill(5))    # '00042'
print("-42".zfill(5))   # '-0042'

print('%05d' % (42))    # '00042'
print('%5d' % (42))     # '   42' 
print('%+5d' % (42))    # '  +42'
print('%-5d' % (42))    # '42   '

print('%20d' % (12))  # right justified
print('%+20d' % (12))  # right justified with + sign in output
print('%-20d' % (12))  # left justified 
print('%020d' % (12))  # filling with leading zeros


print()
print('Python'.center(25))
print('Python'.center(25, '-'))
print('Python'.center(25, '.'))

print()
print('Python'.ljust(25))
print('Python'.ljust(25, '-'))
print('Python'.ljust(25, '.'))

print()
print('Python'.rjust(25))
print('Python'.rjust(25, '-'))
print('Python'.rjust(25, '.'))

'''
>>> 'name'.isidentifier()
True
>>> 'name123'.isidentifier()
True
>>> 'name_some'.isidentifier()
True
>>> 'name123_TWO'.isidentifier()
True
>>> 'PI'.isidentifier()
True

>>> '2name'.isidentifier()
False
>>> 'name 1'.isidentifier()
False

>>> 'name_1'.isidentifier()
True
>>> '_job'.isidentifier()
True
>>> '_val'.isidentifier()
True
>>> '__name__'.isidentifier()
True
'''
