#!/usr/bin/python
"""
Purpose: Demonstration of Palindrome check 
"""

my_string1 = 'manam' #'adda' # 'mom', 'dad'

my_string2 = my_string1[::-1]


print(my_string1,my_string2)

if my_string1 == my_string2:
    print('It is a palindrome string')

# assignment : get the string in runtime and validate
# assignment: display all palindrome numbers btwn 0 and 2000
