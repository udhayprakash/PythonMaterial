#!/usr/bin/python3
"""
Purpose: Check even-ness of a given number, in runtime.
"""

# Logic: determining odd/even status using the modulus arithmetic operator
number = 34
print(f'{number             = }')
print(f'{number / 2         = }')
print(f'{number % 2         = }')
print(f'{number % 2 == 0    = }')

if number:
    print(f'{number} is non-zero')

if number != 0:
    print(f'{number} is non-zero')

if number % 2:  # number % 2 != 0
    print(f'{number} is odd')

if number % 2 == 0:
    print(f'{number} is Even')

# --------------------
print()
number = 13
print(f'{number             = }')
print(f'{number % 2         = }')
print(f'{number % 2 == 0    = }')

if number % 2:  # number % 2 != 0
    print(f'{number} is odd')

if number % 2 == 0:
    print(f'{number} is Even')


# Rewriting with else
if number % 2:
    print(f'{number} is ODD')
else:
    print(f'{number} is EVEN')

# rewriting
if number % 2 == 0:
    print(f'{number} is EVEN')
else:
    print(f'{number} is ODD')

# Assignment: Generate even numbers between 45 & 137
# loop values between limits, test eveness for each number
# and display , if it is even
