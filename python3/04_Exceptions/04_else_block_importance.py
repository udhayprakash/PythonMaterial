#!/usr/bin/python3
"""
Purpose: Addition operation, with exception handling
    Importance of "else" block
"""

# # Case 1 - without exception handling
# num1 = 1000
# num2 = 2022

# add_result = num1 + num2
# print(f"{add_result = }")


# num1 = 1000
# num2 = "2022"
# add_result = num1 + num2
# # print(f"{add_result = }")  TypeError: unsupported operand type(s) for +: 'int' and 'str'


try:
    num1 = int(input("Enter an integer:"))
    num2 = int(input("Enter an integer:"))
except Exception as ex:
    print(f"Error is {ex=}")
else:
    result = num1 + num2
    print(result)
finally:
    print("-------FINALLY-----------------")

print("-------NEXT STATEMENT-----------")

# NOTE: In this problem context, finally is not needed
