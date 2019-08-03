#!/usr/bin/python
"""
Purpose: range()

these will work only with int type 
range(initialValue, finalValue, step)
default initialValue = 0
default step = +1
"""
list(range(0))                     # []
list(range(1, 0))                  # []

r = range(0, 20, 2)
print(r)                           # range(0, 20, 2)

r.start                            # 0
r.stop                             # 20
r.step                             # 2

11 in r                            # False
10 in r                            # True

r.count(11)                        # 0
r.count(10)                        # 1
r.index(10)                        # 5

r[5]                               # 10
r[:5]                              # range(0, 10, 2)
r[-1]                              # 18

range(0) == range(2, 1, 3)         # True
range(0, 3, 2) == range(0, 4, 2)   # True
