#!/usr/bin/python
"""
Purpose: divmod() function 
    divmod(x,y) returns x//y, x%y 

"""
print("10 / 2         =", 10 / 2)   # true division
print("10 // 2        =", 10 // 2)  # Quotient
print("10 % 2         =", 10 % 2)   # remainder
print("divmod(10,2)   =", divmod(10, 2))

print()
print("10 / 3         =", 10 / 3)   # true division
print("10 // 3        =", 10 // 3)  # Quotient
print("10 % 3         =", 10 % 3)   # remainder
print("divmod(10,3)   =", divmod(10, 3))

print()
# print("divmod( 3+4j, 2) =", divmod(3 + 4j, 2))
# TypeError: can't take floor or mod of complex number.


# To get last digit in an integer
print(divmod(45676, 10))
print(divmod(4567, 10))
print(divmod(456, 10))
print(divmod(45, 10))
print(divmod(4, 10))
