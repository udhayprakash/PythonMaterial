#!/usr/bin/python
"""
Purpose: Number Guessing Game

luckyNumber = 67
"""

guessingNumber = int(raw_input('Enter a number:'))
# print 'type(guessingNumber)', type(guessingNumber)
print 'You entered ', guessingNumber

luckyNumber = 67

if (luckyNumber == guessingNumber):
    print 'You Guessed the Correct Number!'
elif (luckyNumber > guessingNumber):
    print 'You Guessed lesser number!'
else:
    print 'You Guessed greater number!'

# else:
#     print 'Try Again!'
