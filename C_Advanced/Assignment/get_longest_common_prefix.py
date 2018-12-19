#!/usr/bin/python
"""
Purpose: Program to find the longest common prefix between a set of words

    input: {'amerigo', 'americ', 'ame', 'america'}
    output: 'ame'
"""
import doctest


def common_prefix(string1, string2):
    if string1 == string2:
        return string1
    common_string = ''
    for index, char1 in enumerate(string1):
        if len(string2) <= index or char1 != string2[index]:
            break
        common_string += char1
    return common_string


def computation(data):
    """
    >>> computation({'amerigo', 'americ', 'ame', 'america', 'ame'})
    'ame'
    >>> computation({'apple', 'ape', 'april'})
    'ap'
    """
    return reduce(lambda x, y: common_prefix(x, y), sorted(data))


if __name__ == '__main__':
    doctest.testmod()
