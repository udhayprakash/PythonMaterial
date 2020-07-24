#!/usr/bin/python3
"""
Purpose: Demonstration of Palindrome check 

    palindrome strings 
        dad
        mom

Algorithms:
-----------
Step 1: Take the string in run-time and store in a variable
Step 2: Compute the reverse of that string
Step 3: Check whether both the strings are equal or not
Step 4: If equal, print that it is palindrome string
"""
test_string = input('Enter any string:')
print(test_string)

# reverse string 
reverse_string = test_string[::-1]
print(reverse_string)

if test_string == reverse_string:
    print( test_string, 'is palindrome')
else:
    print( test_string, 'is NOT a palindrome')