#!/usr/bin/python3
"""
Purpose: To check whether the given character 
        is vowels or consonant

        vowels - aeiou
"""

letter = input('Enter an english alphabet:').strip()

# using the membership opertor - 'in'
# Method 1
if letter in 'aeiouAEIOU':
    print(f'{letter} is a vowel.')
else:
    print(f'{letter} may be a consonant')

# Method 2
if letter.lower() in 'aeiou':
    print(f'{letter} is a vowel.')
else:
    print(f'{letter} may be a consonant')
