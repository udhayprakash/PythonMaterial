#!/usr/bin/python
"""
Purpose: Number Guessing Game

luckyNumber = 67
"""
__author__ = 'Python Tutor'

luck_number = 67

guessing_no = int(input('Enter guessing number:'))

# print(guessing_no, type(guessing_no))

# if guessing_no == luck_number:
#     print('YOU WON THE GAME')
# else:
#     print('Please try again !!!!')

if guessing_no == luck_number:
    print('You WON THE GAME')
elif guessing_no > luck_number:
    print('reduce your guessing number')
else:
    print('increase your guessing number')
