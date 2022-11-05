#!/usr/bin/python3
"""
Purpose: Exception Handling

    Exception Hierarchy
"""

# try:
#     num1 = int(input("Enter an integer:"))
#     num2 = int(input("Enter an integer:"))
#     division = num1 / num2
# except Exception as ex:
#     print(f"{ex =}")
#     print("Please enter integers only (or) denominator is 0")
# else:
#     print(f"{division = }")


try:
    num1 = int(input("Enter an integer:"))
    num2 = int(input("Enter an integer:"))
    division = num1 / num2
except ValueError as ve:
    print(f"{ve =}")
    print("Please enter integers only")
except ZeroDivisionError as ze:
    print(f"{ze =}")
    print("Denominator should be NON-zero")
except Exception as ex:
    print(f"Unhandled Exception: {ex =}")
else:
    print(f"{division = }")
