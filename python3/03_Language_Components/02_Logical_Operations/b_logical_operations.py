#!/usr/bin/python3
"""
Purpose: Logical Operations
    Chaining Comparsion(Relational) Operators
"""
print("23 <73 <45", 23 < 73 < 45)
#   23 <73  and     73 <45
#     True  and       False = False

print("89 <73 <99", 89 < 73 < 99)

print("0 <73 <99", 0 < 73 < 99)  # True

print("89 <73 <99< 999< 0", 89 < 73 < 99 < 999 < 0)
# 89 <73 and 73 <99 and 99< 999 and  999< 0
#  False and  True  and  True   and   False  = False

print("1<2<3<4<5", 1 < 2 < 3 < 4 < 5)
# 1 < 2 and 2 < 3 and 3 < 4 and 4 < 5
# True  and True  and True  and True = True

print(f"{11 == 11 == 11 =}")  # True
print(f"{11 != 12 != 13 =}")  # False
print(f"{11 != 12 != 11 =}")  # True
