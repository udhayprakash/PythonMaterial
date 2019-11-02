#!/usr/bin/python
"""
Purpose: Number Guessing Game

"""
__author__ = 'Python Tutor'

lucky_number = 67

# guessed_number = int(input('GUess a no. between 1 to 100:'))

# if guessed_number == lucky_number:
#     print('YOU GUEssed CORRECTly !!!')
# elif guessed_number > lucky_number:
#     print('Reduce your guess')
# else:
#     print('increase your guess')


# attempts = 0
# while attempts < 5:
#     guessed_number = int(input('GUess a no. between 1 to 100:'))

#     if guessed_number == lucky_number:
#         print('YOU GUEssed CORRECTly !!!')
#         break
#     elif guessed_number > lucky_number:
#         print('Reduce your guess')
#     else:
#         print('increase your guess')
#     attempts += 1

#     if attempts == 5:
#         print('Sorry! you exceeded your 5 chances !!!!')

attempts = 0
while attempts < 5:
    guessed_number = int(input('GUess a no. between 1 to 100:'))

    if guessed_number == lucky_number:
        print('YOU GUEssed CORRECTly !!!')
        break
    elif guessed_number > lucky_number:
        print('Reduce your guess')
    else:
        print('increase your guess')
    attempts += 1

else:
    # This block executes when all loops of while/for are executed
    print('Sorry! you exceeded your 5 chances !!!!')


# while 1:
#     guessed_number = int(input('GUess a no. between 1 to 100:'))

#     if guessed_number == lucky_number:
#         print('YOU GUEssed CORRECTly !!!')
#         break
#     elif guessed_number > lucky_number:
#         print('Reduce your guess')
#     else:
#         print('increase your guess')

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
    
'''
Assignment
------------------------
attempts        points
-----------------------
1-3             100
4-9              60
10-16            20
17-25             5
26-               0
'''