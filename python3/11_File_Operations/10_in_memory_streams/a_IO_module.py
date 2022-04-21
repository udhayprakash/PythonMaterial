#!/usr/bin/python
"""
Purpose: StringIO Module
    - Implements an in-memory file like object.
    - This object can then be used as input or
      output to most functions that would expect
      a standard file object.

cStringIO is c based implementation for StringIO,
which is faster.

In Python 3, these both modules are replaced with io module
"""
try:
    from StringIO import StringIO ## for Python 2
except ImportError:
    from io import StringIO ## for Python 3


# Arbitrary string
message = 'This is just a normal string\n'

# Use StringIO method to set as file object
f = StringIO(message)

data = f.read()
print('Data:', data)

f.write('Second line written to file like object')

print(f'\n current cursor postion is {f.tell()}')
print('Again', f.read())

f.seek(0)
print(f'\n current cursor postion is {f.tell()}')
print('Again', f.read())

f.close()
# f.read()
# ValueError: I/O operation on closed file
