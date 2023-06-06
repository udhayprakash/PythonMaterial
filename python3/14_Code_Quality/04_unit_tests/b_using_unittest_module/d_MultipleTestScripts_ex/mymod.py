"""
Purpose:
    anagram
        cat <--> act
"""


def is_anagram(a_word, b_word):
    """
    >>> is_anagram('cat', 'act')
    True
    >>> is_anagram('tom', 'mat') is not True
    True
    """
    return sorted(a_word) == sorted(b_word)
