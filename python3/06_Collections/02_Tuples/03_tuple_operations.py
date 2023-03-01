#!/usr/bin/python3
"""
Purpose: Tuple operations
"""
# Tuple concatenation

# Python is strictly type language
#   - operation is possible with same/similar types only
result = (9, 99) + (99,)
print("result   :", result)

result = ((9, 99) + (99,),)
print("result   :", result)

# result = (9, 99) + (99,),,
# SyntaxError: invalid syntax

result = ((9, 99) + ((99,),),)
print("result   :", result)

result = (9, 99) + (11, 1)
print("result   :", result)

# result = (9, 99) + [11, 1]
# TypeError: can only concatenate tuple (not "list") to tuple

result = (9, 99) + tuple([11, 1])
print("result   :", result)

result = list((9, 99)) + [11, 1]
print("result   :", result)


# working on strings
print(f"{list('Python')  =}")
print(f"{tuple('Python') =}")

# Tuple repetition
print(f"{(1,) * 3      =}")
print(f"{(1, 2) * 3    =}")
print(f"{(1, (2,)) * 3 =}")


# Assignment
# 1. Prove that tuple concatenation is not commutative: t1 + t2 != t2 + t1
# 2. Prove that tuple repetition is commutative       : t1 * 3 == 3 * t1
