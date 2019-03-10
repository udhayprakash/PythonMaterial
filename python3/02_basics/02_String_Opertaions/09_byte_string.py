#!/usr/bin/python
"""
Purpose: demo of byte strings
    bytes objects actually behave like 
    immutable sequences of integers, with each 
    value in the sequence restricted such that 
    0 <= x < 256
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
my_list = [1, 2, 3, 4, 5]

b_list = bytes(my_list)
print(b_list, type(b_list))

##########################################
# bytes to string 
print(b'hello'.decode('utf-8'))

o_string = b_string.decode('utf-8')
print(o_string, type(o_string))

o_string = str(b_string, 'utf-8')
print(o_string, type(o_string))

# ascii, utf-8, utf-16, cp-232