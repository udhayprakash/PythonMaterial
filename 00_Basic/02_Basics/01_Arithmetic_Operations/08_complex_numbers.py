#!/usr/bin/python
"""
Purpose: Demonstration of complex numbers

Complex Number = Real Number +/- Imaginary Number

In python, 'j' is used to represent the imaginary number.
"""

num1 = 2 + 3j
print "num1=", num1
print "type(num1)=", type(num1)

print
num2 = 0.0 - 2j
print "num2 = ", num2
print "type(num2) = ", type(num2)

print
num3 = 1.0 - 0j
print "num3 = ", num3
print "type(num3) = ", type(num3)

print
num4 = - 0j
print "num4 = ", num4
print "type(num4) = ", type(num4)

print 
print 4j
# print j4 # NameError: name 'j4' is not defined

# NOTE: 4\*j, j4, j*4 are not possible. 
# In these cases, interpreter treats 'j' as a variable.

print "num1.real + num2.imag =", num1.real + num2.imag 
# print "num1.real + num2.imag * j =", num1.real + num2.imag * j
            # NameError: name 'j' is not defined
print "num1.real + num2.imag * 1j = ", num1.real + num2.imag * 1j

# complex()  - Builtin function
print "complex(2,-3.456)", complex(2,-3.456)      
print "complex(2,0)", complex(2,0)      

# == checks value equivalence
print "(3 + 4j) == (4j + 3)= ", (3 + 4j) == (4j + 3)
