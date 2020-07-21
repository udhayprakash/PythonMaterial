#!/usr/bin/python
"""
Purpose: To check whether the given character 
        is vowels or consonant
"""

letter = input("Enter a letter: ")
 
# using the membership operator 'in'
if letter in 'aeiouAEIOU':  
    print(letter, "is a vowel.")
else:
    print(letter, "is a consonant.")
