#!/usr/bin/python
"""
Purpose: Number Guessing Game

"""
__author__ = 'Python Tutor'
lucky_number = 67

# attempts = 0
# while attempts < 5:
#     attempts += 1
#     print(f'\nThis is attempt no: {attempts}')
#     guessed_number = int(input('Enter a no. between 0 & 100:'))

#     if guessed_number < lucky_number:
#         print('Increase your guessing number')
#     elif guessed_number > lucky_number:
#         print('Reduce your guessing number')
#     else:
#         print('You GUESSED CORRECTLY!!!')
#         break
# else:
#     print('Sorry! You are unable to Guess within {attempts} attempts')



while 1:
    guessed_number = int(input('\nEnter a no. between 0 & 100:'))

    if guessed_number < lucky_number:
        print('Increase your guessing number')
    elif guessed_number > lucky_number:
        print('Reduce your guessing number')
    else:
        print('You GUESSED CORRECTLY!!!')
        break

    choice = input('Enter Y(or y) to continue:').upper()
    if choice != 'Y':
        break
