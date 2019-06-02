#!/usr/bin/python
"""
Purpose: Exception handling demo 

try 
except 
else  - optional block 
finally - optional block 

case 1" when no exception 
           try -> else -> finally 
case 2: when there is exception
            try > except -> finally 
"""
name =  'asdasd'
try:
    result = name + 1/ 10 
except  ZeroDivisionError as ex:
    print(' ZeroDivisionError occrred. Error is',repr(ex))
except  TypeError as ex:
    print(' TypeError occrred. Error is',repr(ex))
except  NameError as ex:
    print(' NameError occrred. Error is',repr(ex))
except  Exception as ex:
    print(' Exception occrred. Error is', repr(ex))
else:
    print('In else block , result =', result)
finally:
    print('IN finally block ')

print('next statement')

# Assignment 
# ------------
# 1. grcery store app, 
#     if user enters quantity in words, instead of numbers, handle it 
#     And come out of the script immediately 
    
