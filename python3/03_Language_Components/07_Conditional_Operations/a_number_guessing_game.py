#!/usr/bin/python
"""
Purpose: Number Guessing Game
"""
LUCKY_NUMBER = 69

# given_number = 69
given_number = int(input('Enter no. between 0 & 100:'))

print(f'{LUCKY_NUMBER = }')
print(f'{given_number = }')

# print(f'{given_number == LUCKY_NUMBER  =}')

# # ------------------------------------------
# if given_number == LUCKY_NUMBER :
#     print('You Guessed Correctly!')

# # ------------------------------------------
# if given_number == LUCKY_NUMBER :
#     print('You Guessed Correctly!')
# else:
#     print('Please Try Again!!')

# ------------------------------------------
if given_number == LUCKY_NUMBER :
    print('You Guessed Correctly!')
elif given_number > LUCKY_NUMBER:
    print('Please Try Again with reducing your guess number')
elif given_number < LUCKY_NUMBER:
    print('Please Try Again with increasing your guess number')

# NOTE: else block is optional in python
