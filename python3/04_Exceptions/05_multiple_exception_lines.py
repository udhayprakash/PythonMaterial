#!/usr/bin/python
"""
Purpose: Exception Handling
"""
try:
    num1 = int(input("Enter an integer:"))
    num2 = int(input("Enter an integer:"))  # 12.3 -- TypeError
except Exception as ex:
    print(f"{ex =}")
    print("Please enter integers only")
else:
    try:
        division = num1 / num2  # ZeroDivisionError
    except Exception as ex1:
        print(f"{ex1 =}")
        print("Denominator cant be zero")
    else:
        print(f"{division = }")

# NOTE: Its recommended to place statements which may be prone to exceptions

# Best practice -- write all exception probable code in try block
print()

try:
    num1 = int(input("Enter an integer:"))
    num2 = int(input("Enter an integer:"))
    division = num1 / num2
except Exception as ex:
    print(f"{ex =}")
    print("Please enter integers only")
else:
    print(f"{division = }")
