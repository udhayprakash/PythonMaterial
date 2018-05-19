#!/usr/bin/python
"""
Purpose: Number Guessing Game

luckyNumber = 67
"""
__author__ = 'Python Tutor'

# guessingNumber = int(raw_input('Enter a number:'))
# print 'type(guessingNumber)', type(guessingNumber)
# print 'You entered ', guessingNumber

luckyNumber = 67

choice = 'y'
print choice.lower() != 'n'
while (choice.lower() != 'n'):
    print choice.lower() != 'n'
    guessingNumber = int(raw_input('Enter a number:'))
    if (luckyNumber == guessingNumber):
        print 'You Guessed the Correct Number!'
        break;  # to exit a loop
    elif (luckyNumber > guessingNumber):
        print 'You Guessed lesser number!'
    else:
        print 'You Guessed greater number!'

    choice = raw_input('Enter N or n to exit:')  # Y
# else:
#     print 'Try Again!'
