#!/usr/bin/python
"""
Purpose: Logical Operations


and - if  all are True, result is True 
or  - if any one of them is True, result is True
not - negate the existing value 
"""

# and,  or,  not  

expr1 = (12 > 34) and (99 >= 9) or ((12 > 34) and (99 >= 9))
#        False    and   True    or  ( False    and      True)
#                False          or            False
print(expr1)

'''
and
---
True and True = True

'''
print('and operation ')
print("True and True  ", True and True)       # True
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
print("True     ", True)
print("not True ", not True)
print("not False ", not False)

print('=============================')

expr2 = (45 <= 45) or (3 > 333)
#          True    or   False  = True
print(expr2)

expr2 = (45 <= 45) or (3 > 333) and (9 == 9)
#       True       or   False   and    True
#       True       or           False  = True
print(expr2)

# left to right and top to bottom


print('23 <73 <45', 23 <73 <45)
                  # 23 <73 and 73 <45
                  #    True and  False = False


print('89 <73 <99', 89 <73 <99)

print('0 <73 <99', 0 <73 <99)


print('89 <73 <99< 999< 0', 89 <73 <99< 999< 0)
# 89 <73 and 73 <99 and 99< 999 and  999< 0
#  False and  True  and  True   and  False   = False

print('1<2<3<4<5', 1<2<3<4<5)
# 1 < 2 and 2 < 3 and 3 < 4 and 4 < 5
# True  and True  and True  and True = True

# Assignment
expr3 = 0 and 1         # 0
print('expr3=', expr3)

expr4 = 3 and 9         # 9
print('expr4=', expr4)


"""
Memory 
    - RAM ===========
        - HEap Memory
            - Application specific private heap
                - BUiltin 
                    True, False, ...
                - user defined 
                    

    - ROM === BIOS 
    - HDD/SDD === non-voltile 
"""