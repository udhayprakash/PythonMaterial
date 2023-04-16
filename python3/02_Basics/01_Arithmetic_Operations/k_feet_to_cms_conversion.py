#!/usr/bin/python3
"""
Purpose: Feet to centimetres conversion

    1 foot = 12 inches
    1 inch = 2.54 centimetres

Algorithm:
----------
Step 1: Get feet values in runtime
Step 2: compute  from feet to cms
            feet to inches, then
            inches to centimeters conversion
Step 3: Display the results
"""
# Constants
FOOT_TO_INCHES = 12
INCHES_TO_CMS = 2.54

print("How tall are you in feet and inches?")
feet = float(input("Feet:"))

inches = FOOT_TO_INCHES * feet
centimeters = INCHES_TO_CMS * inches

centimeters = round(centimeters, 2)

print("Your height in centimetres:", centimeters, "cm")
