#!/usr/bin/python
"""
Purpose: Logical Operations
    - Will result in a boolean value (True or False)

    and - if  all are True, result is True
    or  - if any one of them is True, result is True
    not - negate the existing value

"""
__name__ = 'Author'

'''
and
---
True and True = True

'''
print('and operation ')
print("True and True  ", True and True)  # True
print("True and False ", True and False)
print("False and True  ", False and True)
print("False and False ", False and False)
print()

'''
or
---
False or False = False

'''
print('or operation ')
print("True or True  ", True or True)
print("True or False ", True or False)
print("False or True  ", False or True)
print("False or False ", False or False)

print()

expr1 = (12 > 34) and (99 >= 9) or ((12 > 34) and (99 >= 9))
#        False    and   True    or (False     and  True    )  -> PEMDAS
#        False    and   True    or           False            -> operator precedence
#                 False         or           False            = False
print(f'{expr1=}')


print()
print("True     ", True)
print("not True ", not True)
print("False    ", False)
print("not False ", not False)
print()

# --------------------
expr2 = (45 <= 45) or (3 > 333)
#         True     or   False     = True
print(f'{expr2 =}')

expr3 = (45 <= 45) or (3 > 333) and (9 == 9)
#         True     or    False  and   True
#         True     or           False       = True
print(f'{expr3 =}')

expr4 = (45 <= 45) or (3 > 333) or (9 == 9)
#          True    or    False  or   True
#                  True         or   True   = True
#  NOTE: Execution flow: left to right and top to bottom
print(f'{expr4 =}')