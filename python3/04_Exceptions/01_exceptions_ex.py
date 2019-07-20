#!/usr/bin/python
"""
when no error - try - else   - finally
when error    - try - except - finally
"""

# result = 1 // 0 
# result = 1 / 0 
# result = 1 % 0 

try:
    result = 1 % 0 
except:
    print('Please dont divide by zero')

try:
    result = 1 % 0 
except Exception:
    print('Please dont divide by zero')

try:
    result = 1 % 0 
except Exception as ex:
    print('error is ', ex)
    print('error is ', str(ex))
    print('error is ', repr(ex))

# NOTE: else and finally blocks are optional
try:
    result = 1 % 10 
except Exception as ex:
    print('error is ', ex)
    print('error is ', str(ex))
    print('error is ', repr(ex))
else: 
    print('try block has no error')
finally:
    print('Finally statement')

print('statement outside these blocks')

