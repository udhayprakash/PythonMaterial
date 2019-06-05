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

# Q) The user can retry any number of number 

lucky_number = 67

# while 1:
#     guessed_number = int(input('Enter guessed number(0-99):'))

#     if guessed_number == lucky_number:
#         print('YOu guessed correctly')
#         break
#     elif guessed_number > lucky_number:
#         print('Lower your guess')
#     else:
#         print('Increase your guess')

# choice = 'Y'
# while choice.upper() == 'Y':
#     guessed_number = int(input('Enter guessed number(0-99):'))

#     if guessed_number == lucky_number:
#         print('YOu guessed correctly')
#         break
#     elif guessed_number > lucky_number:
#         print('Lower your guess')
#     else:
#         print('Increase your guess')

#     choice = input('Do you want to try again : Y/N:')





# Q)  Restructing to a particular number of retries 


attempt = 1
while attempt <= 5:
    guessed_number = int(input('Enter guessed number(0-99):'))

    if guessed_number == lucky_number:
        print('YOu guessed correctly')
        break
    elif guessed_number > lucky_number:
        print('Lower your guess')
    else:
        print('Increase your guess')

    attempt += 1
else:
    print('Your 5 retries were completed!!!')