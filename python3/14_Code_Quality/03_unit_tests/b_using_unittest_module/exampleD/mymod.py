#!/usr/bin/python
"""
Purpose:
    anagram
        cat <--> act
"""


def is_anagram(a_word, b_word):
    return sorted(a_word) == sorted(b_word)


if __name__ == '__main__':
    assert is_anagram('cat', 'act') is True
    assert is_anagram('tom', 'mat') is not True
