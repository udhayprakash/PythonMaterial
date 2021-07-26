#!/usr/bin/python3
"""
Purpose: Number Guessing Game
"""
LUCKY_NUMBER = 69

given_number = int(input('Enter no. between 0 & 100:'))

print(f'{LUCKY_NUMBER                   =}')
print(f'{given_number                   =}')

print(f'{given_number == LUCKY_NUMBER   =}')

# # Method 1 - only if condition
# if given_number == LUCKY_NUMBER:
#     print('YOU GUESSED CORRECTLY !!!')

# # Method 2 - with if and else
# if given_number == LUCKY_NUMBER:
#     print('YOU GUESSED CORRECTLY !!!')
# else:
#     print('Please Try Again!')

# Method 3 - with elif ladder
if given_number == LUCKY_NUMBER:
    print('YOU GUESSED CORRECTLY !!!')
elif given_number > LUCKY_NUMBER:  # 78 > 69
    print('Please Try Again with reducing your guess number')
elif given_number < LUCKY_NUMBER:  # 34 < 69
    print('Please Try Again with increasing your guess number')

# NOTE: else block is optional in python
