#!/usr/bin/python
# SyntaxError cant be handled 
# bat = 0
try:
    # result = None/100
    result = 1 / '0' + bat
except ZeroDivisionError as ex:
    print('ZeroDivisionError error is ', ex)
    print('error is ', str(ex))
    print('error is ', repr(ex))
except NameError as ex1:
    print('NameError error is ', ex1)
    print('error is ', str(ex1))
    print('error is ', repr(ex1))
except TypeError as ex1:
    print('TypeError error is ', ex1)
    print('error is ', str(ex1))
    print('error is ', repr(ex1))
except Exception as ex2:
    print('Exception - error is ', ex2)
    print('error is ', str(ex2))
    print('error is ', repr(ex2))
else:
    print('else block -')
    print('result=', result)
finally:
    print('finally block')

# NOTE: when more than one error is present, 
# it return the first error encountered when traversing 
# from left to right and top to bottom approach