#!python -u 
"""
Purpose: Display the crazy numbers

Crazy number: A number whose digits are when raised to the power of the number of digits in that number and then added and if that sum is equal to the number then it is a crazy number.

Example:
Input: 123
Then, if 1^3 + 2^3 + 3^3 is equal to 123 then it is a crazy number.
"""


def crazy_num(n):
    a = b = int(n)
    c = 0  # 'c' is the var that stores the number of digits in 'n'.

    s = 0  # 's' is the sum of the digits raised to the power of the num of digits.

    while a != 0:
        a = int(a / 10)
        c += 1

    while b != 0:
        rem = int(b % 10)
        s += rem ** c
        b = int(b / 10)

    if s == n:
        print ("Crazy number.")
    else:
        print ("Not crazy number.")

    return None


n = int(input("Enter number: "))
crazy_num(n)
