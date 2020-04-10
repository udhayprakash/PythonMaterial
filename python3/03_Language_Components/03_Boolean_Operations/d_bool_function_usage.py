#!/usr/bin/python
"""
Purpose: bool() builtin function
"""
__name__ = 'Author'

num1 = -0.000000056
print('bool(num1)       ', bool(num1))
print('bool(num1 != 0)  ', bool(num1 != 0))

if num1 != 0:  # => bool(num1 != 0) => bool(True) => True
    print('It is non-zero')

if num1:  # => bool(num1 != 0) => bool(True) => True
    print('It is non-zero')

# -------------------------------------------------------
num2 = -0.000000000
print('bool(num2)       ', bool(num2))
print('bool(num2 != 0)  ', bool(num2 != 0))

if num2 != 0:  # => bool(num2 != 0) => bool(False) => False
    print('It is non-zero')

if num2:  # => bool(num2 != 0) => bool(False) => False
    print('It is non-zero')

if not num2 != 0:
    print('It is zero ')

if not num2:  # => bool(not num2) => bool( not num2 != 0) => bool(not False) => bool(True) => True
    print('It is zero ')

# ---------------------------------------------------------
if num1 < 7 and num1 < 8:
    print('num1 < 7 and num1 < 8')

# Step 1: bool(num1 < 7 and num1 < 8)
# Step 2: bool(True     and   True)
# Step 3: bool(True) => True

# not False = True => bool(True) => True
if not (num1 > 7 and num1 < 8):
    print('not (num1 > 7 and num1 < 8)')

# ---------------------------
if num1:  # num1 != 0
    print("a=", num1)

if not 0:
    print("hello")

while 1:
    print("hello")
    break

# -----------------------------
# Question
print("bool('False')", bool('False'))
print("bool(False)  ", bool(False))
