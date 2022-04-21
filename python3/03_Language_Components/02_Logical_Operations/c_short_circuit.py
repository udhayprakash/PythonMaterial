##!/usr/bin/python3
"""
Purpose: short-circuit logic
"""

expr3 = 0 and 1  # 0
print("expr3=", expr3)

expr4 = 3 and 9  # 9
print("expr4=", expr4)

expr4 = 3 and 9 and 13  # 13
print("expr4=", expr4)

expr4 = 3 and 13 and 9  # 9
print("expr4=", expr4)  # and is resulting last element


expr5 = 0 or 1  # 1
print("expr5=", expr5)

expr6 = 3 or 9  # 3
print("expr6=", expr6)

expr6 = 3 or 9 or 13  # 3
print("expr6=", expr6)

expr6 = 13 or 9 or 3  # 13
print("expr6=", expr6)  # or is resulting first element
print()

# and - returns 0, if anyone is 0; else the last value
print(f"{0 and 1 and 2 and 3 = }")  # 0
print(f"{1 and 2 and 3 and 4 = }")  # 4
print(f"{1 and 2 and 0 and 4 = }")  # 0
print(f"{1 and 2 and 3       = }")  # 3
print()

# or - will take first boolean True value
print(f"{0 or 1 or 2 or 3    = }")  # 1
print(f"{1 or 2 or 3 or 4    = }")  # 1
print(f"{4.4 or 2 or 3 or 4  = }")  # 4.4
