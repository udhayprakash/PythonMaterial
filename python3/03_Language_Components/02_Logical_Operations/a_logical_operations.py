#!/usr/bin/python3
"""
Purpose: Logical Operations
    - Will result in a boolean value (True or False)

    and - if  all are True, result is True
    or  - if any one of them is True, result is True
    not - negate the existing value

"""
# and - If all are True, result is True; else False
print('and operation ')
print("True and True  ", True and True)  # True
print("True and False ", True and False)
print("False and True  ", False and True)
print("False and False ", False and False)
print()

# or - If all are False, result is False; else True
print('or operation ')
print("True or True  ", True or True)
print("True or False ", True or False)
print("False or True  ", False or True)
print("False or False ", False or False)  # False

print()
expr1 = (12 > 34) and (99 >= 9) or ((12 > 34) and (99 >= 9))
#        False    and   True    or (  False   and  True    )  # -> PEMDAS
#        False    and   True    or            False           # -> operator predecence
#                 False         or            False           = False
print(f'{expr1=}')
print()

print("True      ", True)
print("not True  ", not True)
print("False     ", False)
print("not False ", not False)
print()

# --------------------
expr2 = (45 <= 45) or (3 > 333)
#         True     or   False     = True
print(f'{expr2 =}')


expr3 = (45 <= 45) or (3 > 333) and (9 == 9)
#          True    or   False   and    True
#          True    or           False       = True
print(f'{expr3 =}')

expr4 = ((45 <= 45) or (3 > 333)) and (9 == 9)
#       (  True    or   False   ) and    True  # PEMDAS
#                  True           and    True = True
print(f'{expr4 =}')

expr5 = (45 <= 45) or (3 > 333) or (9 == 9)
#          True    or    False  or   True
# NOTE: Execution Flow: top-> bottom; left-> right

print(f'{expr5 =}')
