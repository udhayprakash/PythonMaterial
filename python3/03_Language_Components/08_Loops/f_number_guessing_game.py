#!/usr/bin/python
"""
Purpose: Number Guessing Game

break - To come out of any loop (for/while)
"""


LUCKY_NUMBER = 67

# # Method 1 - No limit on number of chances(attempts)
# given_number = int(input('Enter no. between 0 & 100:'))
#
# if given_number == LUCKY_NUMBER:
#     print('You guessed correctly!')
# elif given_number > LUCKY_NUMBER:  # 87 > 67
#     print('Reduce your guessing number')
# else:  # given_number < LUCKY_NUMBER
#     print('Increase your guessing number')

# # Method 2 - To limit the number of attempts
# attempt = 0
# while attempt < 5:
#     attempt += 1
#     print(f'attempt number {attempt}', end='-')
#
#     given_number = int(input('Enter no. between 0 & 100:'))
#
#     if given_number == LUCKY_NUMBER:
#         print('You guessed correctly!')
#         break
#     elif given_number > LUCKY_NUMBER:  # 87 > 67
#         print('Reduce your guessing number')
#     else:  # given_number < LUCKY_NUMBER
#         print('Increase your guessing number')
#
#     if attempt == 5:
#         print(f'Sorry! YOu failed to guess in all {attempt} attempts')


# # Method 3 - while with else condition
# attempt = 0
# while attempt < 5:
#     attempt += 1
#     print(f'attempt number {attempt}', end='-')
#
#     given_number = int(input('Enter no. between 0 & 100:'))
#
#     if given_number == LUCKY_NUMBER:
#         print('You guessed correctly!')
#         break
#     elif given_number > LUCKY_NUMBER:  # 87 > 67
#         print('Reduce your guessing number')
#     else:  # given_number < LUCKY_NUMBER
#         print('Increase your guessing number')
# else:
#     print(f'Sorry! YOu failed to guess in all {attempt} attempts')

# # Method 4 - Check for user choice after each incorrect guess
# while True:
#     given_number = int(input('Enter no. between 0 & 100:'))
#
#     if given_number == LUCKY_NUMBER:
#         print('You guessed correctly!')
#         break
#     elif given_number > LUCKY_NUMBER:  # 87 > 67
#         print('Reduce your guessing number')
#     else:  # given_number < LUCKY_NUMBER
#         print('Increase your guessing number')
#
#     choice = input('Enter Y(or y) to continue .. ').upper()
#     if choice != 'Y':
#         break

# Method 5 - Infinite chances till the correct guess is made
attempt = 0
while True:
    attempt += 1
    print(f'attempt number {attempt}', end='-')
    given_number = int(input('Enter no. between 0 & 100:'))

    if given_number == LUCKY_NUMBER:
        print('You guessed correctly!')
        break
    elif given_number > LUCKY_NUMBER:  # 87 > 67
        print('Reduce your guessing number')
    else:  # given_number < LUCKY_NUMBER
        print('Increase your guessing number')

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
