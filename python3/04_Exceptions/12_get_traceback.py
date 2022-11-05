#!/usr/bin/python3
"""
Purpose: Get the exception traceback
"""
import sys
import traceback

num1 = 12
num2 = 34
num3 = 456
num4 = "34"
num5 = 3445

try:
    expr1 = num1 / num2 - num3
    expr2 = num2 * num4 / num3
    expr3 = num2 - num4
    expr4 = expr1 * (expr2) / expr3
except ZeroDivisionError:
    print("Denominator in divison should not be zero")
except Exception as ex:
    print(f"Unhandled exception:{ex =}")
    # print(" sys.exc_info()",  sys.exc_info())
    exc_type, exc_value, exc_traceback = sys.exc_info()  # TUPLE UNPACKING

    print(
        f"""
    exc_type     : {exc_type},
    exc_value    : {exc_value},
    exc_traceback: {exc_traceback},
        Error Line: {exc_traceback.tb_lineno},
        tb_lasti  : {exc_traceback.tb_lasti},
        tb_next   : {exc_traceback.tb_next}
        tb_frame  : {exc_traceback.tb_frame},
    """
    )
    print()
    traceback.print_exc(file=sys.stdout)
else:
    print(f"{expr4 =}")
finally:
    print("Finally block")

print("next Statement")
