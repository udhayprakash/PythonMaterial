#!/usr/bin/python
"""
Purpose: Number Guessing Game

luckyNumber = 67


while loop syntax:
-----------------
    initilization
    while(condition check):
        logic 
        increment/decrement

example:
--------
    i = 0
    while(i <10):
        print i
        i+=1
"""
__author__ = 'Python Tutor'

# guessingNumber = int(raw_input('Enter a number:'))
# print 'type(guessingNumber)', type(guessingNumber)
# print 'You entered ', guessingNumber

luck_number = 67
chances = 0

while 1:
    if chances == 5:
        print('You exceeded the chances limit.!!!')
        break
    guessed_number = int(input('Guess no. between 1 & 99:'))
    print(f'\nYou Guessed {guessed_number} of datatye {type(guessed_number)}')

    if guessed_number == luck_number:
        print('You guessed correctly!!!!')
        break
    elif guessed_number > luck_number:
        print('please guess further lower number')
    else: # guessed_number > luck_number
        print('please guess further greater number')
    chances = chances + 1



# choice = 'y'

# while (choice.lower() != 'n'):
#     print(choice.lower() != 'n')
#     guessingNumber = int(input('Enter a number:'))
#     if (luckyNumber == guessingNumber):
#         print('You Guessed the Correct Number!')
#         break;  # to exit a loop
#     elif (luckyNumber > guessingNumber):
#         print('You Guessed lesser number!')
#     else:
#         print('You Guessed greater number!')

#     choice = input('Enter N or n to exit:')  # Y
# else:
#     print('Try Again!')

# print('next statement')
