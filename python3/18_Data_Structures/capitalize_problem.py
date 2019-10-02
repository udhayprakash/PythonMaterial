#!/usr/bin/python
"""
Purpose: https://www.hackerrank.com/challenges/capitalize/problem
"""


def solve(s):
    return ' '.join(i.capitalize() for i in s.split(' '))

    # result = []
    # for ech in s.split(' '):
    #     if ech:
    #         if ech[0].isdigit():
    #             result.append(ech)
    #         else:
    #             result.append(ech.capitalize())
    #     else:
    #         result.append(ech)
    # return ' '.join(result)


test_word = (
    'alison heck',
    'chris alan',
    'hello world',
    '1 w 2 r 3g',
    '12abc',
    '1 2 2 3 4 5 6 7 8  9',
    'q w e r t y u i o p a s d f g h j  k l z x c v b n m Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M'
)

for ech in test_word:
    print(ech, solve(ech), sep='\n')

print('Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M')
