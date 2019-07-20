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


# TOTAL_ATTEMPT = 5
# LUCKY_NUMBER = 67

# Q)  Restructing to a particular number of retries 

# attempt = 0
# while attempt < TOTAL_ATTEMPT:
#     attempt +=  1
#     print(f'attempt={attempt}')

#     guessed_no = int(input('Enter no. btwn 0 & 100:'))
#     if guessed_no == LUCKY_NUMBER:
#         print('YOu WON the GAME !!!')
#         break
#     elif guessed_no > LUCKY_NUMBER:
#         print('LOWER your guess')
#     else: 
#         print('INCREASE your guess')
# else:
#     print('YOU FAILED THE GAME')


# for i in range(9):
#     if i == 5:
#         break
#     print(i)
# else: 
#     print('All loops completed')


LUCKY_NUMBER = 67

attempts = 0
choice = 'Y'
while choice == 'Y':
    guessed_no = int(input('Enter no. btwn 0 & 100:'))
    if guessed_no == LUCKY_NUMBER:
        print(f'YOu WON the GAME in {attempts} attempt!!!')
        break
    elif guessed_no > LUCKY_NUMBER:
        print('LOWER your guess')
    else: 
        print('INCREASE your guess')

    attempts +=1

    choice = input('Enter Y to continue:').upper()

# LUCKY_NUMBER = 67

# attempts = 0
# while 1:
#     guessed_no = int(input('Enter no. btwn 0 & 100:'))
#     if guessed_no == LUCKY_NUMBER:
#         print(f'YOu WON the GAME in {attempts} attempt!!!')
#         break
#     elif guessed_no > LUCKY_NUMBER:
#         print('LOWER your guess')
#     else: 
#         print('INCREASE your guess')

#     attempts +=1


# 1st
# 2nd
# 3rd
# 4th
# 5th
# 6th
# 7th
# 8th
# 9th
# 10th
# 11th 
# 12th

