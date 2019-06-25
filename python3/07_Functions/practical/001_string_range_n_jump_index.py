#!/usr/bin/python
"""
Problem statement:

    input : abcdef
    output: a-f $ 1 (where 1 is jump index)

    input : acf
    output: a-f $ 2


Assumption: jump index is constant for an input pattern
"""


def range_n_jump_index(str1):
    temp = '%s-%s $ %d' % (str1[0], str1[-1], ord(str1[1]) - ord(str1[0]))
    return temp


print(range_n_jump_index('abcdef'))

print(range_n_jump_index('acf'))














