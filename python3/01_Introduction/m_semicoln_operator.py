#!/usr/bin/python3
"""
Purpose: Multiple statements in same line
    , logic separator
    ; statement completion operator
"""
print('asdsd', 213, 123 + 123 - 3)

# Method 1
num1 = 100;
num2 = 200
sum_of_numbers = num1 + num2
print('Sum of Number:', sum_of_numbers)

# Method 2
num1 = 100; num2 = 200; sum_of_numbers = num1 + num2; print('Sum of Number:', sum_of_numbers)


# conclusion 
# 1.  ; is optional. Will not change anything
# 2.  ; is important if we need write more than one statement in same line
# 3.  Unnecessarily placing semicolon at end of statement will increase computation time
'''
python -c "print('hello world')"

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