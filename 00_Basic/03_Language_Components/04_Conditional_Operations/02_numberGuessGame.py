#!/usr/bin/python
"""
Purpose: Number Guessing Game

luckyNumber = 67
"""

guessingNumber = int(raw_input('Enter a number:'))
print 'type(guessingNumber)', type(guessingNumber)
print 'You entered ', guessingNumber

luckyNumber = 67

if (guessingNumber == luckyNumber):
    print 'You Guessed the Correct Number!'
else:
    print 'Try Again!'
