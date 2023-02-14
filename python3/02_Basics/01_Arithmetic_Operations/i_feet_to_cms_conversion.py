#!/usr/bin/python3
"""
Purpose: Feet to centimetres conversion

    1 foot = 12 inches
    1 inch = 2.54 centimetres

Step 1: Get feet values in runtime
Step 2: compute  from feet to cms
sTep 3: display the result
"""
print("How tall are you in feet and inches?")
feet = int(input("Feet:"))  # 5
inches = float(input("Inches:"))  # 8

cms = (feet * 12 + inches) * 2.54
print("Your height in centimetres:", cms)
