#!/usr/bin/python3
"""
Purpose: Logical Operations
"""
print('23 <73 <45', 23 < 73 < 45)
#   23 <73  and     73 <45
#     True  and       False = False

print('89 <73 <99', 89 < 73 < 99)

print('0 <73 <99', 0 < 73 < 99)  # True

print('89 <73 <99< 999< 0', 89 < 73 < 99 < 999 < 0)
# 89 <73 and 73 <99 and 99< 999 and  999< 0
#  False and  True  and  True   and   False  = False

print('1<2<3<4<5', 1 < 2 < 3 < 4 < 5)
# 1 < 2 and 2 < 3 and 3 < 4 and 4 < 5
# True  and True  and True  and True = True

# Assignment
expr3 = 0 and 1  # 0
print('expr3=', expr3)

expr4 = 3 and 9  # 9
print('expr4=', expr4)
