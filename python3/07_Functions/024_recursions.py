#!/usr/bin/python
"""
Purpose: Recursive Functions 
"""
# Example - calculating the factorial

def factorial(num):
    """
    factorial(9) = 9 * 8 * 7 * 6 * .....1
    :param num: int
    :return: final sum 
    """
    # print(f'{num =}')
    if num == 1:
        return 1
    return num * factorial(num -1)

result = factorial(9)  # 362880
print(result)

import math


from functools import reduce 
result = reduce(lambda x,y: x*y, range(1, 9 + 1))

assert math.factorial(9) == factorial(9) == result


# Example - Caesar Cipher 
def caesar_cipher(sentence):
    if not sentence:
        return ''
    elif sentence[0] == ' ':
        cipher_char = ' '
    else:
        cipher_char = chr(ord(sentence[0]) + 3)
    # print(f'{sentence[0]} {cipher_char}')
    return cipher_char + caesar_cipher(sentence[1:])

cipher_text = caesar_cipher(
    'war is planned at morning sun rise')
print(cipher_text)

"""
exercises on recursions:
--------------------------
1. Write a recursive function to reverse a list
        input:  [1, 2, 3, 3, 4, 5]
        output: [5, 4, 3, 3, 2, 1]
2. Write a recursive function to compute the fibonacci series
        0,1, 1,2, 3 , 5, 8, ....
        HINT: unpacking
"""
