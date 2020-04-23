#!/usr/bin/python
"""
Purpose: Identity Operations

    =  Assignment operator

    == Value-level Equivalence  -  ( value and type) check
    is object-level Equivalence - (address location, value and type) check

Object
    - value(s)
    - type(s)
    - address location where it is stored - id()


Dual Memory management Strategy
    In Interactive mode,
        For integer,
            -5 to 256  -> no new object created
            outside bounds -> new object is created for each variable
"""


print(f'{4 == 4   = }')
print(f'{4 == "4" = }')

print(f'{4 is 4   = }')
print(f'{4 is "4" = }')
print()

num1 = 100
num2 = 200

print(f'{num1 = }')
print(f'{num2 = }')
print(f'{num1 == num2 = }')
print(f'{num1 is num2 = }')
print(f'{id(num1) = } \t {id(num2) =}')
print()

num1 = 200

print(f'{num1 = }')
print(f'{num2 = }')
print(f'{num1 == num2 = }')
print(f'{num1 is num2 = }')
print(f'{id(num1) = } \t {id(num2) =}')
print()

num3 = 300
num4 = 300
print(f'{num3 =} \t {num4 =}')
print(f'{num3 == num4 = }')
print(f'{num3 is num4 = }')
print(f'{id(num3) = } \t {id(num4) =}')

'''
var1 = 256
var2 = 256
var1 is var2
Out[19]: True
id(var1), id(var2)
Out[20]: (140730434123392, 140730434123392)
var1 = 257
var2 = 257
var1 is var2
Out[23]: False
id(var1), id(var2)
Out[24]: (1659666892848, 1659666892080)
'''

'''
For strings, no new object is created for new variables, 
if already a variable is present with that value
>>> v1 = 'udhay'
>>> v2 = 'udhay'
>>>
>>> id(v1)
35989168
>>> id(v2)
35989168
>>> v2 = 'udhaykjkjkasdkasjdkjasdhkjsahkdjhksjdksajdkdskjashkjdkjashkdjaskjdhkjassssskkjhkjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj'
>>> v1 = 'udhaykjkjkasdkasjdkjasdhkjsahkdjhksjdksajdkdskjashkjdkjashkdjaskjdhkjassssskkjhkjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj'
>>>
>>> v1 is v2
True
'''
