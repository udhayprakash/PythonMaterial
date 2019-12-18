#!/usr/bin/python
# SyntaxError cant be handled 

try:
    # NOne = 23
    val = '0'
    result = NOne + val + 10 / 0
except TypeError as ex2:
    print('for type error', repr(ex2))
except ZeroDivisionError as ex3:
    print('for zero division', repr(ex3))
except NameError as ex4:
    print('for name error', repr(ex4))
except Exception as ex1:
    print('Umbrella exception', repr(ex1))
else:
    print('NO Exception in code')
finally:
    print('finally block')

# exception precedence
#   - python execution flow
#         - left to right & top to botton

# NOTE: when more than one error is present,
# it return the first error encountered when traversing
# from left to right and top to bottom approach

# NOTE: higher the exception, latter it need to be defined

