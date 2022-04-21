#!/usr/bin/python3
"""
Purpose: Handling multiple exceptions together
"""
try:
    expression = eval(input('Enter an expression:'))
except KeyboardInterrupt as ex1:
    print('YOU STOPPED WITH KEYBOARD INTERRUPT')
except (ZeroDivisionError, SyntaxError, TypeError) as ex3:
    print(f'Either zerodivision or syntax issue, or typing error occured:{ex3}')
except Exception as ex:
    print(f'Unhandled exception: {ex=}')
else:
    print(f'{expression =}')

"""
~!python3 08_handling_multiple_exceptions.py
Enter an expression:100/0
Either zerodivision or syntax issue, or typing error occured:division by zero

~!python3 08_handling_multiple_exceptions.py
Enter an expression:654 + '87'
Either zerodivision or syntax issue, or typing error occured:unsupported operand type(s) for +: 'int' and 'str'

~!python3 08_handling_multiple_exceptions.py
Enter an expression:766+ 0007
Either zerodivision or syntax issue, or typing error occured:leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers (<string>, line 1)

~!python3 08_handling_multiple_exceptions.py
Enter an expression:6546547647 ** 7657657658875
YOU STOPPED WITH KEYBOARD INTERRUPT
^C
"""
