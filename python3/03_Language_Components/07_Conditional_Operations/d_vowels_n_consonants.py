#!/usr/bin/python3
"""
Purpose: To check whether the given character
        is vowels or consonant

        vowels - aeiou

in operator  works with any iterable object
"""
letter = input("Enter an english alphabet:").strip()

print(f"{letter =}", letter.isalpha())

if len(letter) != 1:
    print(f"{letter} s INVALID INPUT")
elif not letter.isalpha():
    print(f"{letter} is not an alphabet")
else:
    # in - membership check operator
    # if letter in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
    # if letter.lower() in ["a", "e", "i", "o", "u"]:
    if letter.lower() in "aeiou":
        print(f"{letter} is a vowel")
    else:
        print(f"{letter} may be a consonant")
