#!/usr/bin/python3
"""
Purpose: Calculating the HCF/GCD between two numbers
    HCF - Highest Common Factor

"""

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

hcf = min(first_number, second_number)
while first_number % hcf != 0 or second_number % hcf != 0:
    hcf = hcf - 1

print(f'''Greatest Common Divisor between \
{first_number} and {second_number} is {hcf}''')
