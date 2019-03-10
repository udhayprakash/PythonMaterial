#!/usr/bin/python
"""
Purpose: Python program to check if the input number is prime or not

A positive integer greater than 1 which has no other factors except 1 and 
the number itself is called a prime number. 2, 3, 5, 7 etc. are prime numbers 
as they do not have any other factors. 
But 6 is not prime (it is composite) since, 2 x 3 = 6.
"""
# num = 407

# take input from the user
num = int(raw_input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            print num, "is not a prime number"
            print i, "times", num // i, "is", num
            break
    else:
        print num, "is a prime number"

    # if input number is less than
# or equal to 1, it is not prime
else:
    print num, "is not a prime number"
