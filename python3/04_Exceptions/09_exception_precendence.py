#!/usr/bin/python3
"""
Purpose: Exception Precedence

Python Execution flow:-
     Top to Bottom & Left to Right

"""
try:
    num1 = 100
    # num2 == 200   # NameError
    # 1231 + '123'  # TypeError
    # 100 / 0       # ZeroDivisionError

    num2 = 200
    # num3 = int('123.23')  # ValueError
    num3 = int("123")
    expr = num2 + 100 + 123 + num3 - 2321 / 10
except Exception as e:
    print(f"{e=}")
else:
    print("No expection- So, in else block")

"""
~!python3 09_exception_precendence.py
No expection- So, in else block

~!python3 09_exception_precendence.py
e=NameError("name 'num2' is not defined")

~!python3 09_exception_precendence.py
e=NameError("name 'num2' is not defined")

~!python3 09_exception_precendence.py
e=TypeError("unsupported operand type(s) for +: 'int' and 'str'")

~!python3 09_exception_precendence.py
e=ZeroDivisionError('division by zero')

~!python3 09_exception_precendence.py
e=NameError("name 'num2' is not defined")

~!python3 09_exception_precendence.py
e=TypeError("unsupported operand type(s) for +: 'int' and 'str'")

~!python3 09_exception_precendence.py
e=ZeroDivisionError('division by zero')
"""


# Assignment
# Using input() and eval(), take some expression in run time and solve it
