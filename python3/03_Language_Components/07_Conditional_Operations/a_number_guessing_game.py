#!/usr/bin/python
"""
Purpose: Number Guessing Game

"""
__name__ = 'Author'

LUCKY_NUMBER = 69

# given_number = 34
given_number = int(input('Enter no. between 0 & 100:'))

# print(given_number, LUCKY_NUMBER)
# print(type(given_number), type(LUCKY_NUMBER))

# ------------------------------------------
if given_number == LUCKY_NUMBER:
    print('You Guessed Correctly !!!')

# ------------------------------------------
if given_number == LUCKY_NUMBER:
    print('You Guessed Correctly !!!')
else:
    print('Please Try Again!')

# ------------------------------------------
if given_number == LUCKY_NUMBER:
    print('You Guessed Correctly !!!')
elif given_number > LUCKY_NUMBER:
    print('Please Try Again with reducing your guess number')
elif given_number < LUCKY_NUMBER:
    print('Please Try Again with increasing your guess number')

# NOTE: else block is optional in python
