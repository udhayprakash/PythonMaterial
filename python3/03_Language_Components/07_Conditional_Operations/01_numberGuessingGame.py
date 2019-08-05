#!/usr/bin/python
"""
Purpose: Number Guessing Game

"""
__author__ = 'Python Tutor'

lucky_number  = 78

guessed_number = int(input('Enter no. btwn 0 & 100:'))

# print(guessed_number, type(guessed_number))
# print(lucky_number == guessed_number)

# if lucky_number == guessed_number:
#     print('YOu guessed correctly!'.upper())
# else:
#     print('Please try again!!!'.title())


if guessed_number < lucky_number:
    print('Increase your guessing number!')
elif guessed_number > lucky_number:
    print('Decrese your guessing number!!')
else:
    print('CONGRATULATION ON GUESSING CORRECTLY')

