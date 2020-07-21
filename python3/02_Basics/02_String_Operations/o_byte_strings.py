#!/usr/bin/python
"""
Purpose: byte Strings
"""
my_string = 'Python is interesting.'
print(my_string, type(my_string))

# string with encoding 'utf-8'
b_string = bytes(my_string, 'utf-8')
print(b_string, type(b_string))

# Create a byte of given integer size
size = 5
arr = bytes(size)
print(arr, type(arr))

# Convert iterable list to bytes
my_list = [11, 12, 13, 14, 15]
b_list = bytes(my_list)
print(b_list, type(b_list))

# A zero-filled bytes object of a specified length
print('bytes(10)', bytes(10))

# From an iterable of integers:
print('bytes(range(20))', bytes(range(20)))

# Copying existing binary data via the buffer protocol:
obj = (89, 65, 76)
print('bytes(obj)', bytes(obj))
# bytes objects are sequences of integers (akin to a tuple)


##########################################
# bytes to string 
print(b'hello'.decode('utf-8'))

o_string = b_string.decode('utf-8')
print(o_string, type(o_string))

o_string = str(b_string, 'utf-8')
print(o_string, type(o_string))

# ascii, utf-8, utf-16, cp-232

##########################################
# hex(0-9 A-F) to byte
# skips ASCII whitespaces during conversion
print(bytes.fromhex('2Ef0 F1f2  '))

# bytes object into its hexadecimal representation
print(b'\xf0\xf1\xf2'.hex())
