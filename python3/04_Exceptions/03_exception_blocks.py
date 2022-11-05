#!/usr/bin/python3
"""
Purpose: Exception Handling Blocks

    blocks - try, except, else, finally

    Execution Flow
        1. when no error     -> try -> else   -> finally
        2. when error occurs -> try -> except -> finally

NOTE: else and finally blocks are optional
NOTE:
    1. code which we may result in errors need to be placed in try block
    2. Error handling to corresponding errors need to be placed in except block
    3. If no errors in try block, corresponding actions in else block
    4. placeholder for all restrospective actions correspoding to that in try block
        ex: in try block, socket/file/remote_connect/db_connection was opened
            in finally block, we can close it

"""

# 10 / 0  # ZeroDivisionError: division by zero

try:
    print("In try block")
    # 10 /0
    10 / int(input("Enter a number:"))
except Exception as ex1:
    print(f"In Exception block: {ex1 =}")
else:
    print("In Else block")
finally:
    print("In finally block")

print("next statement")


# # case 1 -- 5  ==========================> NO EXCEPTION
# - python 03_exception_handling.py
# In try block
# Enter a number:5
# In Else block
# In finally block
# next statement

# # case 2 -- 0 ============================> ZeroDivisionError
# - python 03_exception_handling.py
# In try block
# Enter a number:0
# In Exception block: ex1 =ZeroDivisionError('division by zero')
# In finally block
# next statement


# # case 3 -- 5.3  ==========================> ValueError
# - python 03_exception_handling.py
# In try block
# Enter a number:5.3
# In Exception block: ex1 =ValueError("invalid literal for int() with base 10: '5.3'")
# In finally block
# next statement
