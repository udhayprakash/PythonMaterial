#!/usr/bin/python3
"""
Purpose: range() builtin function
"""
list(range(0))  # [] -> range(0, 0, 1)
list(range(1, 0))  # [] -> range(1, 0, 1)
list(range(1, 0, -1))  # [1]

r = range(0, 20, 2)
print(r)  # range(0, 20, 2)-> 0, 2, 4, 6, 8, 10, 12, 14, 16, 18
#                                                      0  1  2  3  4  5    6   7  8   9

r.start  # 0
r.stop  # 20
r.step  # 2

11 in r  # False
10 in r  # True

r.count(11)  # 0
r.count(10)  # 1
r.index(10)  # 5

r[5]  # 10
r[:5]  # range(0, 10, 2)
r[-1]  # 18

range(0) == range(2, 1, 3)  # True
range(0, 3, 2) == range(0, 4, 2)  # True
