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

try:
    print('In try block')
    10 / 0
except Exception as ex:
    print(f'In Exception block: {ex =}')
else:
    print('In Else block')
finally:
    print('In finally block')

print('next statement')
