#!/usr/bin/python
"""
Purpose: Demonstration of complex numbers

Complex Number = Real Number +/- Imaginary Number

In python, 'j' is used to represent the imaginary number.
"""

num1 = 2 + 3j
print("num1=", num1)
print("type(num1)=", type(num1))

print()
num2 = 0.0 - 2j
print("num2 = ", num2)
print("type(num2) = ", type(num2))

print()
print("num1             = ", num1)
print("num1.conjugate() = ", num1.conjugate())
print("num1.real        = ", num1.real)
print("num1.imag        = ", num1.imag)

print()
print("num1 * num2.real = ", num1 * num2.real)
print("(num1*num2).real = ", (num1 * num2).real)

# Observe the signs of imaginary numbers
print('========================================')
print('arithmetic operations on complex numbers')
print('========================================')

print("num1 + num2 = ", num1 + num2)
print("num1 - num2 = ", num1 - num2)
print("num1 * num2 = ", num1 * num2)
print("num1 / num2 = ", num1 / num2)

print()
print("num1 / 2    = ", num1 / 2)