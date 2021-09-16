#!/usr/bin/python3
"""
Purpose: Complex Numbers in Python

    Complex Number = Real Number +/- Imaginary Number

In python, 'j' is used to represent the imaginary number.

"""
num1 = 2
print('num1=', num1, type(num1))

num1 = 2 + 3
print('num1=', num1, type(num1))

num1 = 2 + 3j
print('num1=', num1, type(num1))

num1 = -0.02 + 3.234j
print('num1=', num1, type(num1))

num1 = -0.02 + 0j
print('num1=', num1, type(num1))

num1 = -0.0j
print('num1=', num1, type(num1))

print(4j)
# print(j4)  # NameError: name 'j4' is not defined

# 4 * j        # NameError: name 'j' is not defined
print('4 * 1j', 4 * 1j)

# NOTE: 4*j, j4, j*4 are not possible.
# In these cases, interpreter treats 'j' as a variable.

# complex()  - Builtin function
print("complex(2,-3.456)", complex(2, -3.456))
print("complex(2,0)     ", complex(2, 0))

# == checks value equivalence
print('4 == 4  :', 4 == 4)     # True
print('4 == 4.3:', 4 == 4.3)   # False

print("(3 + 4j) == (4j + 3)= ", (3 + 4j) == (4j + 3))  # True 
print("(3 + 4j) == (4 + 3j)= ", (3 + 4j) == (4 + 3j))  # False

