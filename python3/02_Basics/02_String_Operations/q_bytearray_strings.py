#!/usr/bin/python
"""
Purpose: demo of bytearray strings

bytearray objects are a mutable strings
"""
# Creating an empty instance:
print("bytearray()          ", bytearray())

# Creating a zero-filled instance with a given length:
print("bytearray(10)        ", bytearray(10))

# From an iterable of integers:
print("bytearray(range(10)) ", bytearray(range(10)))

# Copying existing binary data via the buffer protocol:
print("bytearray(b'Hi!')", bytearray(b"Hi!"))

##########################################
# hex to bytearray
print(" bytearray.fromhex('2Ef0 F1f2  ')", bytearray.fromhex("2Ef0 F1f2  "))

# bytearray to hex
print("bytearray(b'\xf0\xf1\xf2').hex()", bytearray(b"\xf0\xf1\xf2").hex())

############################################
# b = bytearray('python') # TypeError: string argument without an encoding
b = bytearray("python", "utf-8")
b = bytearray(b"python")
print(b, type(b))
# b[0] will be an integer,
print(b[0], type(b[0]))
# while b[0:1] will be a bytearray object of length 1
print(b[0:1], type(b[0:1]))
