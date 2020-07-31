#!/usr/bin/python
"""
Purpose: Exception Handling 

    blocks - try, except, else, finally 

    Execution Flow 
        1. when no error     -> try -> else   -> finally
        2. when error occurs -> try -> except -> finally 

NOTE: 
    1. code which we may result in errors need to be placed in try block 
    2. Error handling to corresponding errors need to be placed in except block 
    3. If no errors in try block, corresponding actions in else block 
    4. placeholder for all restrospective actions correspoding to that in try block 
        ex: in try block, socket/file/remote_connect/db_connection was opened 
            in finally block, we can close it 

NOTE: else and finally blocks are optional 
"""
try:
    print('In try block')
    # 10 / 0
    10 / 10
except Exception as ex:
    print('In except block')
    print(f'\t{ex =}')
else:
    print('No error. So, in else block')
finally:
    print('In finally block')

print('next statement')
