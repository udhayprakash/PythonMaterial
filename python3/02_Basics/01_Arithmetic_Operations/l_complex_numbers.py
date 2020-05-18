#!/usr/bin/python
"""
Purpose: complex numbers in Python

"""
num1 = 0.0 - 2j
num2 = 2 + 3j 

# dir() -> Gives list of attributes associated with an object

# pen - Object 
#       -> Uses  - writing, painting, .....

# Phone - Object 
        # -> uses   - pics with cam 
        #           - communications 
        #           - alaram 
        #           - watch 

print('num1 =', num1, type(num1))

print(dir(num1)) # ['conjugate', 'imag', 'real']

print("num1             = ", num1)   # 0 -2j
print("num1.real        = ", num1.real)  # 0.0
print("num1.imag        = ", num1.imag)  # -2.0

# CONJUGATE  will result  same number with change in sign of imaginary part
print("num1.conjugate() = ", num1.conjugate())   # 
print("num2.conjugate() = ", num2.conjugate())   # 2 - 3j 

print()
print("num1 * num2.real = ", num1 * num2.real)   # PEMDAS
print("num1 *(num2.real)= ", num1 * (num2.real))

print("(num1*num2).real = ", (num1 * num2).real)
