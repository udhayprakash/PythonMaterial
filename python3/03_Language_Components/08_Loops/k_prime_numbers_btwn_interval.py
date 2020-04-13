#!/usr/bin/python
"""
Purpose: program to display all the prime numbers within an interval
"""
__name__ = 'Author'

lower = 90
upper = 1000

# lower = eval(input("Enter lower range: "))
# upper = eval(input("Enter upper range: "))

print(f'Prime numbers between {lower} and {upper} are:')

for num in range(lower, upper + 1):
    # prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num, end=' ')
