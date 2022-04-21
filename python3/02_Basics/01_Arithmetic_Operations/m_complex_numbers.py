#!/usr/bin/python
"""
Purpose: complex numbers in Python

"""
num1 = 0.0 - 2j
num2 = 2 + 3j

# pen - Object
#         - shape, color, texture
#       -> Uses  - writing, painting, drawing.....

# Cell Phone - Object
#         - shape, color
# -> uses   - pics with cam
#           - communications
#           - alaram
#           - watch

# Object Oriented Programming
# Object
#   - Address - where it is stored
#   - type    - of the object
#   - value   - present in that object

print("num1      =", num1)  # Value
print("type(num1)=", type(num1))  # data type
print("id(num1)  =", id(num1))  # Addrress location

print("dir(num1) =", dir(num1))  # Usage - attributes
# 'conjugate', 'imag', 'real'

print("num1             = ", num1)  # -2j
print("num1.real        = ", num1.real)  # 0.0
print("num1.imag        = ", num1.imag)  # -2.0

# CONJUGATE  will result  same number with
# change in sign of imaginary part
print("num1.conjugate() = ", num1.conjugate())  # 2j
print("num2.conjugate() = ", num2.conjugate())  # 2 - 3j
print("(-2 -3j).conjugate()", (-2 - 3j).conjugate())  # -2 +3j

print()
print("num1 * num2.real = ", num1 * num2.real)  # PEMDAS
print("num1 *(num2.real)= ", num1 * (num2.real))

print("(num1*num2).real = ", (num1 * num2).real)
