#!/usr/bin/python3
"""
Purpose: Arithmetic Operations

    Integer Family
        - int
        - long -> only in python 2.x
        - float

        - complex
        - bool
"""
# + - * / // %
# NOTE: PEP 8 recommends to place one space around the operator

# = assignment operator
num1 = 100  # int
num2 = 123  # int

num3 = num2
# 1233 = num4 # SyntaxError: cannot assign to literal

print("num1 =", num1, type(num1))
print("num2 =", num2, type(num2))
print("num3 =", num3, type(num3))

# 1. Addition
num3 = num1 + num2  # int + int = int
print("num3 =", num3, type(num3))
print()

num4 = -1.0  # float
print("num4=", num4, type(num4))

num4 = 1.0  # float
print("num4=", num4, type(num4))

num4 = -1.2342342342  # float
print("num4=", num4, type(num4))

num5 = num1 + num4  # int + float = float
print("num5=", num5, type(num5))

# Question 1: what is the largest number that can be processed in python
num6 = 9999999956456434344343242343232423423423423423423432432423434123232323
print("num6=", num6, type(num6))

# Question 2: what is the smallest number that can be processed in python
num6 = 0.00002130213869388792183798798321989812739
print("num6=", num6, type(num6))

print()
# ---------------------------------------
# Arithmetic Operations
print("123 + 100 = ", 123 + 100)
print("123 - 100 = ", 123 - 100)
print("123 * 100 = ", 123 * 100)
print("123 / 100 = ", 123 / 100)

print()
print("10/2 = ", 10 / 2)
print("10/5 = ", 10 / 5)
print("10/3 = ", 10 / 3)
# NOTE: division result will be floating point every time

"""
3 ) 10  ( 3.3
     9
    --
     10
      9
    ---

3) 10(3  <-- Quotient  //
    9
   --
    1  <-- Remainder  %
"""
print()
print("10 // 3 = ", 10 // 3)  # quotient - floor division
print("10 % 3  = ", 10 % 3)  # remainder - modulo division
print("divmod(10, 3)=", divmod(10, 3))  # //, %

"""
10/2

    2 ) 10 ( 5  <-- Quotient
        10
        ---
         0  <--- remainder

"""
print()
print("10 // 2      =", 10 // 2)
print("10 % 2       =", 10 % 2)
print("divmod(10, 2)=", divmod(10, 2))  # //, %


# IMPORTANCE OF SIGNS
print()
print("10 / 3   = ", 10 / 3)  # 3.3333333333333335
print("-10 / 3  = ", -10 / 3)  # -3.3333333333333335
print("10 / -3  = ", 10 / -3)  # -3.3333333333333335
print("-10 / -3 = ", -10 / -3)  # 3.3333333333333335

print()
# The result is always rounded towards minus infinity
print("10 // 3   = ", 10 // 3)  # 3     3 <  3.333 < 4
print("-10 // 3  = ", -10 // 3)  # -4    -4 < -3.333 < 3
print("10 // -3  = ", 10 // -3)  # -4    -4 < -3.333 < 3
print("-10 // -3 = ", -10 // -3)  # 3     3 <  3.333 < 4

print()
print("10 % 3   = ", 10 % 3)  # 1
print("-10 % 3  = ", -10 % 3)  # 2
print("10 % -3  = ", 10 % -3)  # -2
print("-10 % -3 = ", -10 % -3)  # -1
