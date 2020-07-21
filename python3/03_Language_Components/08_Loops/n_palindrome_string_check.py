#!/usr/bin/python
"""
Purpose: To check whether given string is palindrome or not 
"""

# 'Anna','Civic','Kayak','Level','Madam','Mom','Noon','Racecar','Radar','Redder','Refer','Repaper','Rotator','Rotor','Sagas','Solos','Stats','Tenet','Wow'

given_str = 'racecar'

# Method 1
if given_str == given_str[::-1]:
    print(f'{given_str} is Palindrome string')

# Method 2
for index in range(0, len(given_str)):
    print(f'{given_str[index]} <--{index}--> {given_str[-index-1]}')
    if given_str[index] != given_str[-index-1]:
        break 
else:
    print(f'{given_str} is Palindrome string')


# Assignment: Display all palindrome primes till 1 crore