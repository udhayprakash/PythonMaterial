#!/usr/bin/python
"""
Purpose: Using Custom Exceptions
"""
# creating a custom exception
class InvalidAge(Exception):
    pass 


try:
    age = int(input('Enter your age:'))
    age = abs(age)
    if age < 18:
        # raise InvalidAge('You are not eligible for voting')
        raise InvalidAge(f'You are short by {18 - age} years for voting')
except InvalidAge as ex:
    print(str(ex))
except ValueError:
    print('Please enter valid age number')
except Exception as ex:
    print('Unhandled Exception -', repr(ex))
else:
    print('Eligible for voting!!!')


# Assignment: create custom Temperature Exception, 
# and check if inputted temperature is suitable for 
# humans. Humans can bear -15 to 50 degree celsius