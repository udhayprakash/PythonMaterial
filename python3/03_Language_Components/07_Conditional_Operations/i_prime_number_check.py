#!/usr/bin/python3
"""
Purpose: Python program to check if the input number is prime or not

    A positive integer greater than 1 which has no other factors except 1 and
    the number itself is called a prime number. 2, 3, 5, 7 etc. are prime numbers
    as they do not have any other factors.
    But 6 is not prime (it is composite) since, 2 x 3 = 6.

    2,  3, 5, 7, 11, ...
"""

# num = 10
num = int(input('Enter any positive number:'))

# Method 1
for i in range(2, num):
    print(i, num % i)
    if num % i == 0:
        print(f'{num} is a composite number')
        break
else:
    print(f'{num} is a PRIME number')

# Method 2
import math 
print(f'{math.sqrt(num) =}')

for i in range(2, int(math.sqrt(num)) + 1):
    print(i, num % i)
    if num % i == 0:
        print(f'{num} is a composite number')
        break
else:
    print(f'{num} is a PRIME number')

print('End of program -------')