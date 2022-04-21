#!/usr/bin/python3
"""
Purpose: String Attributes
"""
print('42'.zfill(5))    # '00042'
print('-42'.zfill(5))   # '-0042'

print('%05d' % (42))    # '00042'
print('%5d' % (42))     # '   42'
print('%+5d' % (42))    # '  +42'
print('%-5d' % (42))    # '42   '
print('%-05d' % (42))   # '42   '

print('%20d' % (12))   # '                  12' right justified
print('%+20d' % (12))  # '                 +12' right justified with + sign in output
print('%-20d' % (12))  # '12                  ' left justified
print('%020d' % (12))  # '00000000000000000012' filling with leading zeros


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
>>> 'name_some_1'.isidentifier()
True
>>> 'name_some_TWO'.isidentifier()
True
>>> 'PI'.isidentifier()
True
>>> 'DOZEN'.isidentifier()
True
>>>
>>>
>>> '2name'.isidentifier()
False
>>> '$name'.isidentifier()
False
>>> 'first-name'.isidentifier()
False
>>> ''.isidentifier()
False
>>>
>>>
>>> '_val'.isidentifier()
True
>>> '_-val'.isidentifier()
False
>>> '__val'.isidentifier()
True
>>> '__val__'.isidentifier()
True
>>> '__name__'.isidentifier()
True
>>> '__________name__'.isidentifier()
True
'''
