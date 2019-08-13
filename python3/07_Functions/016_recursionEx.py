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
    if len(word) == 1:
        return word[0]
    return string_reversal(word[1:]) +  word[0]
        
print(string_reversal('Python'))



def string_reversal(word):
    if len(word) == 1:
            return word[0]
    return word[-1] + string_reversal(word[:-1])
        
print(string_reversal('Python'))




# factorial(9) = 9 *8 * 7 * 6 * .....1

def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num -1)

print(factorial(9))
import math
print('math.factorial(9)', math.factorial(9))


def ceaser_cipher(mystring):
    if mystring == '':
        return ''
    return  chr(ord(mystring[0]) + 3)  + ceaser_cipher(mystring[1:])

print(ceaser_cipher('This is good'))



