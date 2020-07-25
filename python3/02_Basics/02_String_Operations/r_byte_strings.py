#!/usr/bin/python
"""
Purpose: byte strings
    bytes objects actually behave like 
    immutable sequences of integers, with each 
    value in the sequence restricted such that 
    0 <= x < 256
"""
# Question: bytearray vs bytes

# bytearray('Python:αλεπού', 'ascii')
# UnicodeEncodeError: 'ascii' codec can't encode
#  characters in position 7-12: ordinal not in range(128)

bytearray('Python:αλεπού', 'utf-8')
# bytearray(b'Python:\xce\xb1\xce\xbb\xce\xb5\xcf\x80\xce\xbf\xcf\x8d')

bytes('Python:αλεπού', 'utf-8')
# b'Python:\xce\xb1\xce\xbb\xce\xb5\xcf\x80\xce\xbf\xcf\x8d'

# ----------------------------------------
my_string = 'Python is interesting.'
print(my_string, type(my_string))

# string with encoding 'utf-8'
b_string = bytes(my_string, 'utf-8')
print(b_string, type(b_string))

# bytes to string 
print(b'hello'.decode('utf-8'))

o_string = b_string.decode('utf-8')
print(o_string, type(o_string))

o_string = str(b_string, 'utf-8')
print(o_string, type(o_string))

# ascii, utf-8, utf-16, cp-232

# In [6]: bytes('udhay', 'ascii')
# Out[6]: b'udhay'

# In [6]: bytes('udhay', 'utf-8')
# Out[6]: b'udhay'

# In [8]: str(b'udhay')
# Out[8]: "b'udhay'"

# In [9]: str(b'udhay', 'utf-8')
# Out[9]: 'udhay'

##########################################
# hex(0-9 A-F) to byte
# skips ASCII whitespaces during conversion
print(bytes.fromhex('2Ef0 F1f2  '))

# bytes object into its hexadecimal representation
print(b'\xf0\xf1\xf2'.hex())
