#!/usr/bin/python
"""
Purpose: Program to check Armstrong numbers in certain interval

A positive integer is called an Armstrong number of order n if
    abcd... = an + bn + cn + dn + ...

ex: 153 = 1*1*1 + 5*5*5 + 3*3*3  --- 153 is an Armstrong number.
"""
# lower = 100
# upper = 2000

# To take input from the user
lower = int(raw_input("Enter lower range: "))
upper = int(raw_input("Enter upper range: "))

for num in range(lower, upper + 1):

    # order of number
    order = len(str(num))

    # initialize sum
    sum1 = 0

    # find the sum of the cube of each digit
    temp = num
    while temp > 0:
        digit = temp % 10
        sum1 += digit ** order
        temp //= 10

    if num == sum1:
        print(num)
