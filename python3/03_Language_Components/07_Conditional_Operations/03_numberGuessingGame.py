#!/usr/bin/python
"""
Purpose: Number Guessing Game

luckyNumber = 67
"""
__author__ = 'Python Tutor'

luck_number = 67

guessed_number = int(input('Guess no. between 1 & 99:'))
print(f'You Guessed {guessed_number} of datatye {type(guessed_number)}')


if guessed_number == luck_number:
    print('You guessed correctly!!!!')
elif guessed_number > luck_number:
    print('please guess further lower number')
else: # guessed_number > luck_number
    print('please guess further greater number')
