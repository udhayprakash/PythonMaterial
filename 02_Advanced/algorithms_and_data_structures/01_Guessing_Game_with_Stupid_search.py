#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randrange

"""
Purpose: Stupid Search.

In a list of numbers, user guesses a number.
    if it is correct, all is good. Else, next time, he/she will guess among the unguessed numbers.
"""
__author__ = "Udhay Prakash Pethakamsetty"

list_of_numbers = range(10, 20)

winning_number = randrange(10, 20)  # place this statement in while loop, to increase probability of failure

# attempts = len(list_of_numbers)

while True:
    try:
        # attempts -= 1
        guess_number = int(raw_input('Guess a number between 10 and 20:'))

        if guess_number == winning_number:
            print 'You Guessed correctly'
            break
        else:
            list_of_numbers.remove(guess_number)
            # print 'Your guess is closer by ', abs(guess_number - winning_number)
            print 'You guessed larger number' if guess_number > winning_number else 'You guessed lower number'

        if len(list_of_numbers) == 1:  # attempts <= 1:
            print 'You are STUPID. Use your brain.'
            print 'Max. attempts completed. The winning number is', list_of_numbers[0]

    except Exception:
        print 'You STUPID! Guess properly'
        # all exceptions are catched here, as user should not know the problem
