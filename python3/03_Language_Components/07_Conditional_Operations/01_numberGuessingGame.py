#!/usr/bin/python
"""
Purpose: Number Guessing Game

"""
__author__ = 'Python Tutor'

lucky_number = 69

# given_number = 56
given_number = int(input('Enter any no. betwn 1 & 100:'))

if given_number == lucky_number:
    print('You guessed correctly!!')

if given_number == lucky_number:
    print('You guessed correctly!!')
else:
    print('PLease try again!')

# NOTE: else block is optional in python


if given_number == lucky_number:
    print('You guessed correctly!!')
elif given_number > lucky_number:   # 70 > 69
    print('Decrease your guessing number')
elif given_number < lucky_number:   # 34 < 69
    print('Increase your guessing number')