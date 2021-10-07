#!/usr/bin/python3
"""
Purpose: sys module 
"""
import sys 

print(f''' 
    {sys.maxsize                    =}
    {sys.maxunicode                 =}
    {sys.byteorder                  =}
    {sys.dllhandle                  =}
    {sys.float_repr_style           =}
    {sys.hash_info                  =}
    {sys.hexversion                 =}

''')

var1 = 9223372036854775807
print(f'{var1 =}')

var1 +=1
print(f'{var1 =}')

# NOTE: sys.maxsize - depends on machine


# sys.maxunicode
print(f'{ord("A")=}')
print(f'{chr(65) =}')

# for i in range(128):
#     print(f'{i =} {chr(i) =}')


# for i in range(1500, 2700):
#     print(f'{i =} {chr(i) =}')

print(f'{chr(1114111) =}')
try:
    print(f'{chr(1114112) =}')
except ValueError as ex:
    print(ex)
    print('YOu entered value exceeding sys.maxunicode')


#    128  64   32  16  8 4  2 1
# 14   0   0    0   0  1 1  1 0
#  7   0   0    0   0  0 1  1 1
# 19   0   0    0   1  0 0  1 1

# byte - 8 bits (or) 2 nibbles
# sys.byteorder - 'little' - lower nibble in right


print(3.33333)
print(10/3)
print(str(10/3))
print(repr(10/3))
print(f'{10/3!s} {10/3!r}')

print(f'{hash(1232) =}')
print(f'{hash(12.32) =}')
print(f'{hash(None) =}')

print(f'{hex(213) =}')
