#!/usr/bin/python
"""
Purpose: To consume the calculator script
"""
import calculator

print(calculator)

help(calculator)

print(dir(calculator))

print(f'calculator.addition(10, 20)     :{calculator.addition(10, 20)}')
print(f'calculator.subtraction(10, 20)  :{calculator.subtraction(10, 20)}')