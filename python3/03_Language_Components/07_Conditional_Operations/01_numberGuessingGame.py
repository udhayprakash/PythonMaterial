#!/usr/bin/python
"""
Purpose: Number Guessing Game

luckyNumber = 67
"""
__author__ = 'Python Tutor'

luckyNumber = 67

guessingNumber = int(input('Enter a number:'))
print('type(guessingNumber)', type(guessingNumber))
print('You entered ', guessingNumber)


if (guessingNumber == luckyNumber):
    print('You Guessed the Correct Number!')
else:
    print('Try Again!')