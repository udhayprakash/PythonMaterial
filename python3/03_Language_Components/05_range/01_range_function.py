#!/usr/bin/python
"""
Purpose: range()

these will work only with int type 
range(initialValue, finalValue, step)
default initialValue = 0
default step = +1
"""

values = range(9) # range(finalValue)
print(values)
print('type(values):', type(values))

values1 = range(0, 9) # range(initialValue, finalValue)
print(values1)

values2 = range(0, 9, 1)  # range(initialValue, finalValue, step)
print(values2)

# 0 1 2 3 4 5 6 7 8
print(list(values2))
print(tuple(values2))

values3 = range(0, 9, 2)  # range(initialValue, finalValue, step)
print(values3)  # 0 2 4 6 8
print(list(values3))

values4 = list(range(9, 0, -1))  # builtin function
print(list(values4))  # 9 8 7 6 5 4 3 2 1

values4 = list(range(9, 0, -2))  # builtin function
print(list(values4)) # 9 7 5 3 1

values6 = range(0, 9, -1)  # range(initialValue, finalValue, step)
print(values6)
print(list(values6))

# values7 = range(0, 9, 1.5)  # range(initialValue, finalValue, step)
# values7 = range(0.5, 9.5, 1)  # range(initialValue, finalValue, step)


for i in range(0, 9, 1):
    print(i)


val = range(9)
print(val[0])