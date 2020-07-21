#!/usr/bin/python
"""
Purpose: Byte String operations 
"""
b = b'python'
print(b, type(b))

# Indexing 
print('b[0]  =', b[0], type(b[0]))

# Slicing 
print('b[0:3]=', b[0:3], type(b[0:3]))

# STRING OPERATIONS ==========
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
print(b'mississippi'.rstrip(b'ipz'))

print(b'1,2,3'.split(b','))
print(b'1,2,3'.split(b',', maxsplit=1))
print(b'1,2,,3,'.split(b','))

print(b'1 2 3'.split())
print(b'1 2 3'.split(maxsplit=1))
print(b'   1   2   3   '.split())

print(b'%(language)s has %(number)03d quote types.' % \
      {b'language': b"Python", b"number": 2})

print('Taj' + "Mahal")
# print('Taj' + b"Mahal")
print(bytes('Taj', 'utf-8') + b"Mahal")
