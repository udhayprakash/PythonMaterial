#!/usr/bin/python
"""
Purpose: Number Guessing Game

"""
__author__ = 'Python Tutor'

lucky_number = 69

# given_number = 56
given_number = int(input('Enter any no. betwn 1 & 100:'))

if given_number == lucky_number:
    print('You Guessed correctly')
else:
    print('Please try again !!!')

if given_number == lucky_number:
    print('You Guessed correctly')
elif given_number < lucky_number:
    print('Increase your guessing no.!')
elif given_number > lucky_number:
    print('Decrease your guessing no.!')

# NOTE: else block is optional in python