#!/usr/bin/python
"""
Purpose: Python program to check if the input number is prime or not

    A positive integer greater than 1 which has no other factors except 1 and
    the number itself is called a prime number. 2, 3, 5, 7 etc. are prime numbers
    as they do not have any other factors.
    But 6 is not prime (it is composite) since, 2 x 3 = 6.

    2,  3, 5, 7, 11, ...
"""
import math 

# num = 23

# take input from the user
num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num <= 1:
    print(num, "is not a prime number")
else:
    # check for factors
    # for factor in range(2, num):
    for factor in range(2, int(math.sqrt(num))):
        if (num % factor) == 0:
            print(num, "is not a prime number")
            print(factor, "times", num // factor, "is", num)
            break
    else:
        print(num, "is a prime number")
