#!/usr/bin/python
"""
Purpose: Demonstration of Palindrome check 
"""

my_string1 = 'adda'

my_string2 = my_string1[::-1]


print(my_string1,my_string2)

if my_string1 == my_string2:
    print('It is a palindrome string')