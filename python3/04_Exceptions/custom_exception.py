#!/usr/bin/python
"""
Purpose: Using Custom Exceptions
"""

class InvalidAge(Exception):
    pass 

age = int(input('Enter voter age:'))

age = abs(age) # Converting to positive 

try:
    if age < 18:
        raise InvalidAge(f'You are short by {18 - age} years for voting')
except InvalidAge as ex:
    print(ex)
else:
    print('Eligible for voting!!!')


# Assignment: create custom Temparature Exception, 
# and check if inputted temperature is suitable for 
# humans. Humans can bear -15 to 50 degree celsius