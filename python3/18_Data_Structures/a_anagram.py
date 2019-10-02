#!/usr/bin/python 
"""
Purpose: Program to validate whether an entered word is anagram
"""
from datetime import datetime


def anagram_validation_pythonic(test_word):
    return test_word == test_word[::-1]


start_time = datetime.now()
print(anagram_validation_pythonic('otto'))
print(datetime.now() - start_time)


#  Implementing without string slicing 

def anagram_validation_without_slicing(test_word):
    str_len = len(test_word)
    for index, ch in enumerate(test_word):
        if ch != test_word[str_len - index - 1]:
            return False
    return True


start_time = datetime.now()
print(anagram_validation_without_slicing('otto'))
print(datetime.now() - start_time)
