#!/usr/bin/python

lucky_number = 88

guessed_number = int(input('Enter guessed number (0-99):'))

# import pdb; pdb.set_trace()
breakpoint()

if guessed_number == lucky_number:
    print('You guessed correctlly')
elif guessed_number > lucky_number:
    print('you guessed greater number')
else:
    print('You guessed lower number')
