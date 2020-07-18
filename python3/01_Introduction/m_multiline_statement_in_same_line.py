#!/usr/bin/python
"""
Purpose: Multiple statements in same line

; statement completion operator
, logic separator
"""

print('asdsd', 213, 123+ 123 - 3)

num1 = 123;
num2 = 300

sum_of_numbers = num1 + num2 

print('Sum of Number:', sum_of_numbers)


# -----------------------------------------------------
num1 = 123; num2 = 300; sum_of_numbers = num1 + num2; print('Sum of Number:', sum_of_numbers)


# conclusion 
# 1.  ; is optional. Will not change anything
# 2.  ; is important if we need write more than one statement in same line
# 3.  Unnecessarily placing semicolon at end of statement will increase computation time
'''
python -c "num1 = 123; num2 = 300; sum_of_numbers = num1 + num2; print('Sum of Number:', sum_of_numbers)"


langauge
    - scripting language  Ex: batch, shell, ....
    - General Purpose programming langauge Ex: c, c++, java, 

Python is both scripting and General purpose programming language


.bat
    cd dirctory1
    cd subdirectory2
    ping google.com > result.txt
'''