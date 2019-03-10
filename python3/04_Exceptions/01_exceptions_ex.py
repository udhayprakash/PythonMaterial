#!/usr/bin/python
"""
when no error - try - else  - finally
when error    - try - except - finally
"""
# result = 1 /0
try:
    result = 1 / 0
except Exception as ex:
    print('error is ', ex)
    print('error is ', str(ex))
    print('error is ', repr(ex))
else:                               # optional block
    print('result=', result)
finally:                            # optional block
    print("finally")

print("next statement")

