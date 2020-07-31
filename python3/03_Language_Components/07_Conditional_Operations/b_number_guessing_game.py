#!/usr/bin/python3
"""
Purpose: Number Guessing Game
"""
LUCKY_NUMBER = 69

given_number = int(input('Enter no. of between 0 & 100:'))

print(f'{LUCKY_NUMBER = }')
print(f'{given_number = }')

# print(f'{given_number == LUCKY_NUMBER  =}')

# Method 1
# if given_number == LUCKY_NUMBER:
#     print('You Guessed Correctly!')

# Method 2
# if given_number == LUCKY_NUMBER:
#     print('You Guessed Correctly!')
# else:
#     print('Please Try Again!!')

# Method 3
if given_number == LUCKY_NUMBER:
    print('You Guessed Correctly!')
elif given_number > LUCKY_NUMBER:  # 78 > 69
    print('Please Try Again with reducing your guess number')
elif given_number < LUCKY_NUMBER:  # 34 < 69
    print('Please Try Again with increasing your guess number')

# NOTE: else block is optional in python
