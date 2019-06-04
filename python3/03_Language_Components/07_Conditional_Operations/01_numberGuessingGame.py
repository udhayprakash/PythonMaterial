#!/usr/bin/python
"""
Purpose: Number Guessing Game

luckyNumber = 67
"""
__author__ = 'Python Tutor'

luck_number = 67

# guessing_number = 89 
guessing_number = int(input('Guess a number (0-100):'))

# if luck_number == guessing_number:
#     print('YOu guessed correct!!!')
# else:
#     print('PLease try again!!!!') 


if guessing_number > luck_number:
    print('You guessd a greater number ')
elif guessing_number < luck_number:
    print('You guessed lesser number')
else:
    print('YOu guessed correctly !!!!')