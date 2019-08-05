#!/usr/bin/python
"""
Purpose: Number Guessing Game

"""
__author__ = 'Python Tutor'
lucky_number = 67

# attempt = 1
# while attempt <= 5:
#     print(f'\nThis is attempt: {attempt}')
    
#     guessed_number = int(input('Enter a number btwn 0 & 100:'))
#     # print(guessed_number, type(guessed_number))

#     if guessed_number > lucky_number:
#         print('Lower your guess')
#     elif guessed_number < lucky_number:
#         print('Increase your guess')
#     else:
#         print('You GUessed correctly')
#         break

#     attempt += 1
# else:
#     print('Sorry! you lost all chances')


choice = 'y'
while choice == 'y':
    guessed_number = int(input('Enter a number btwn 0 & 100:'))

    if guessed_number > lucky_number:
        print('Lower your guess')
    elif guessed_number < lucky_number:
        print('Increase your guess')
    else:
        print('You GUessed correctly')
        break

    choice = input('\nEnter y to continue:').lower()
