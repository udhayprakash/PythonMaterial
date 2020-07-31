#!/usr/bin/python3
"""
Purpose: Check eveness of given number in runtime
"""


# Logic: determining odd/even status using the modulus arithmetic operator
number = 34
print(f'{number =}')
print(f'{number % 2 =}')
print(f'{number % 2 == 0 =}')

if number % 2 == 0:
    print('It is Even')
else:
    print('It is odd')
print()

number = 13
print(f'{number =}')
print(f'{number % 2 =}')
print(f'{number % 2 == 0 =}')

if number % 2 == 0:
    print('It is Even')
else:
    print('It is odd')


number = int(input('Enter any valid number:'))
print(f'{number =}')
print(f'{number % 2 =}')
print(f'{number % 2 == 0 =}')

if number % 2 == 0:
    print('It is Even')
else:
    print('It is odd')


# Assignment: Generate even numbers between 45 & 137
