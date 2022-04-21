#!/usr/bin/python
"""
Purpose: Feet to centimetres conversion

    1 foot = 12 inches
    1 inch = 2.54 centimetres
"""

print("How tall are you in feet and inches?")
feet = int(input("Feet: "))
inches = float(input("Inches: "))

cms = (feet * 12 + inches) * 2.54
print("Your height in centimetres:", cms)
