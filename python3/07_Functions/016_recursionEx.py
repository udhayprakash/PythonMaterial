# #!/usr/bin/python
# """
# Purpose: 


# Three Laws of Recursion:
# ------------------------
# 1. A recursive algorithm must have a base case.
# 2. A recursive algorithm must change its state and move toward the base case.
# 3. A recursive algorithm must call itself, recursively.

# pseudo-code:
# -------------
# def funcName(<input paramaters>):
#     <some condition check for termination>
#     <some logic>
#     return funcName(<input parameters>)


# Recursion is a programming technique in which a call to a function results in another call to that same function.
# Iteration is calling an object, and moving over it.

# """


# # calculating sum of a list of numbers

# def sumOfList(num_list):  # conventional implementation
#     total = 0
#     for i in num_list:
#         total += i
#     return total

# print(sumOfList([12, 23, 34, 546, 1]))


# def sumOfListRec(num_list):  # implementation using recursions
#     if len(num_list) == 1:
#         return num_list[0]
#     else:
#         return num_list[0] + sumOfListRec(num_list[1:])

# print(sumOfListRec([12, 23, 34, 546, 1]))

# """
# exercises on recursions:
# --------------------------
# 1. Write a recursive function to compute the factorial of a number
#         factorial(10) = 10 * 9 * 8 * 7 * 6 * 5, ..... 1
# 2. Write a recursive function to reverse a list
#         input:  [1, 2, 3, 3, 4, 5]
#         output: [5, 4, 3, 3, 2, 1]
# 3. Write a recursive function to compute the fibonacci series
#         0,1, 1,2, 3 , 5, 8, ....
#         HINT: unpacking
# """

def string_reversal(word):
    if not word:
        return ''
    return word[-1] + string_reversal(word[:-1])


result = string_reversal('Python')
print(result)


def string_reversal_1(word):
    if not word:
        return ''
    return string_reversal_1(word[1:]) + word[0]


result = string_reversal_1('Python')
print(result)


# -----------------------------------

def factorial(num):
    """
    factorial(9) = 9 * 8 * 7 * 6 * .....1
    :param num:
    :return:
    """
    if num == 1:
        return 1
    return num * factorial(num - 1)


result = factorial(9)  # 362880
print(result)

import math

assert math.factorial(9) == factorial(9)


# ------------------------------
def caesar_cipher(sentence):
    if not sentence:
        return ''
    if sentence[0] == ' ':
        cipher_char = sentence[0]
    else:
        cipher_char = chr(ord(sentence[0]) + 3)
    return cipher_char + caesar_cipher(sentence[1:])


cipher_text = caesar_cipher('war is planned at morning sun rise')
print(cipher_text)
