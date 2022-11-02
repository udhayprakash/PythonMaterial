#!/usr/bin/python3
"""
Purpose: To check whether the given character
        is vowels or consonant

        vowels - aeiou

in operator  works with any iterable object
"""
letter = input("Enter an english alphabet:").strip().lower()

# using the membership operator - 'in'
# Method 1
if letter in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
    print(f"{letter} is a vowel")
else:
    print(f"{letter} may be a consonant")


# Method 2
if letter.lower() in ["a", "e", "i", "o", "u"]:  # list - iterable object
    print(f"{letter} is a vowel")
else:
    print(f"{letter} may be a consonant")


# Method 3
if letter.lower() in "aeiou":
    print(f"{letter} is a vowel")
else:
    print(f"{letter} may be a consonant")
