#!/usr/bin/python
"""
Purpose: demo of byte strings
"""
# Other uses of byte string 

# A zero-filled bytes object of a specified length
print('bytes(10)', bytes(10))

# From an iterable of integers: 
print('bytes(range(20))', bytes(range(20)))

# Copying existing binary data via the buffer protocol:
obj = (89,65, 76)
print('bytes(obj)', bytes(obj))
# bytes objects are sequences of integers (akin to a tuple)

#############################
# hex to byte
# skips ASCII whitespaces suring conversion
print(bytes.fromhex('2Ef0 F1f2  '))

# bytes object into its hexadecimal representation
print(b'\xf0\xf1\xf2'.hex())

################################
b = b'python'
print(b, type(b))
# b[0] will be an integer, 
print(b[0], type(b[0]))
# while b[0:1] will be a bytes object of length 1
print(b[0:1], type(b[0:1]))



##### STRING OPERATIONS
# ordinary strings
a = "abc"
b = a.replace("a", "f")

# bytes and bytearray strings
a = b"abc"
b = a.replace(b"a", b"f")

print(b'Py' in b'Python')
print(b'   spacious   '.lstrip())
print(b'www.example.com'.lstrip(b'cmowz.'))
print(b'   spacious   '.rstrip())
print( b'mississippi'.rstrip(b'ipz'))


print(b'1,2,3'.split(b','))
print(b'1,2,3'.split(b',', maxsplit=1))
print(b'1,2,,3,'.split(b','))

print(b'1 2 3'.split())
print(b'1 2 3'.split(maxsplit=1))
print(b'   1   2   3   '.split())


print(b'%(language)s has %(number)03d quote types.' %\
           {b'language': b"Python", b"number": 2})