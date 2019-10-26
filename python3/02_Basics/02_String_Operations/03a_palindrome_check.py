#!/usr/bin/python
"""
Purpose: Demonstration of Palindrome check 
"""
test_string =  input('Enter any string:') #'dad' #'mom'

# print(test_string)
# print(test_string[::-1])

if test_string == test_string[::-1]:
    print(test_string, 'is a palindome string')
else:
    print(test_string, 'is not a palindrome string')

# assignment : display all palindrome numbers btwn 0 and 2000. HINT: str()
#     0, 1, 2, 3, 4, 5, 6,7, ... 11, 22, ... 222, 333