#!/usr/bin/python3
"""
Purpose: Identity Operations

    Object
        - value(s)
        - type(s)
        - address location where it is stored - id()


    =  Assignment operator

    == Value-level Equivalence  -  ( value and type) check
    is object-level Equivalence - (address location, value and type) check

Dual Memory management Strategy
    In Interactive mode,
        For integer,
            -5 to 256      -> no new object created
            outside bounds -> new object is created for each variable

- Python preallocates small integers in a range of -5 to 256.
- This allocation happens during initialization and since
   we cannot update integers (immutability) these preallocated
   integers are singletons and are directly referenced instead
   of reallocating.
- This means every time we use/creates a small integer, python instead
   of reallocating just returns the reference of preallocated one.

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
print()

num3 = 300.33
num4 = 300.33
print(f'{num3 =} \t {num4 =}')
print(f'{num3 == num4 = }')
print(f'{num3 is num4 = }')
print(f'{id(num3) = } \t {id(num4) =}')
print()

num3 = 'Udhay'
num4 = 'Udhay'
print(f'{num3 =} \t {num4 =}')
print(f'{num3 == num4 = }')
print(f'{num3 is num4 = }')
print(f'{id(num3) = } \t {id(num4) =}')
print()

num3 = [1, 2, 3]
num4 = [1, 2, 3]
print(f'{num3 =} \t {num4 =}')
print(f'{num3 == num4 = }')
print(f'{num3 is num4 = }')
print(f'{id(num3) = } \t {id(num4) =}')
