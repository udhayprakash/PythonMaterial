#!/usr/bin/python
"""
Purpose: Number Guessing Game

luckyNumber = 67
"""
__author__ = 'Python Tutor'

luck_number = 67


guessed_number = int(input('guessed number='))

# if guessed_number == luck_number:
#     print('YOu guessed correctly!!!!!!')
# elif guessed_number != luck_number:
#     print('Please guess again!!!!!!')
# else: 
#     print('Else condition meet')


if guessed_number == luck_number:
    print('YOu guessed correctly!!!!!!')
elif guessed_number > luck_number:
    print('guessed_number > luck_number')
elif guessed_number < luck_number:
    print('guessed_number < luck_number')

#NOTE: else is optional in python 