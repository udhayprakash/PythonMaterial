#!/usr/bin/python

"""
Purpose: Demonstration of Arithmetic Operations


Integer family
	int
	long  - python 2 only 
	float

	complex
	bool
"""

# + - * / // %
# NOTE: PEP 8 recommends to place one space around the operator

num1 = 123 # int
num2 = 100 # int 

print('num1=', num1)
print('num2=', num2)

num3 = num1 + num2 # int + int = int 
print('num3=', num3, type(num3))

num4 = -1.2342342342
print('num4=', num4, type(num4))

# what is the largest number that can be processed in python
num5 = 123123213123123231232312312312313453454534
print('num5=', num5, type(num5))

num5 = 123123213123123231232312312312313453454534.0
print('num5=', num5, type(num5))

####### 
# Arithemtic Operations
print("123 + 100 = ", 123 + 100)
print("123 - 100 = ", 123 - 100)
print("123 * 100 = ", 123 * 100)
print("123 / 100 = ", 123 / 100)

print()
print('10/2 = ', 10/2)
print('10/5 = ', 10/5)
print('10/3 = ', 10/3)
# NOTE: division result will be floating point everytime

print('10 // 3 = ', 10 // 3)# quotient - floor division
print('10 % 3 = ', 10 % 3)  # remainder

print('divmod(10, 3)=', divmod(10, 3))# //, %
# 3 ) 10 ( 3 -- QUotient
#      9
# 	--
# 	 1 --- remainder

print('divmod(10, 2)=', divmod(10, 2))# //, %

# IMPORTANCE OF SIGNS
print()
print('10 / 3   = ', 10 / 3)     #  3.3333333333333335
print('-10 / 3  = ', -10 / 3)    # -3.3333333333333335
print('10 / -3  = ', 10 / -3)    # -3.3333333333333335
print('-10 / -3 = ', -10 / -3)   #  3.3333333333333335

print()
# The result is always rounded towards minus infinity
print('10 // 3   = ', 10 // 3)    #  3     3 <  3.333 < 4
print('-10 // 3  = ', -10 // 3)   # -4    -4 < -3.333 < 3
print('10 // -3  = ', 10 // -3)   # -4    -4 < -3.333 < 3
print('-10 // -3 = ', -10 // -3)  #  3     3 <  3.333 < 4

print()
print('10 % 3   = ', 10 % 3)      #  1     
print('-10 % 3  = ', -10 % 3)     #  2
print('10 % -3  = ', 10 % -3)     # -2
print('-10 % -3 = ', -10 % -3)    # -1
