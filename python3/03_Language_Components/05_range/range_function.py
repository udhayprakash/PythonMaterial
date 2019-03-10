#!/usr/bin/python
"""
Purpose: range()

these will work only with int type 
range(initialValue, finalValue, step)
default initialValue = 0
default step = +1
"""

values = range(9)
print(values)
print('type(values):', type(values))

values1 = range(0, 9) # range(initialValue, finalValue)
print(values1)

values2 = range(0, 9, 1)  # range(initialValue, finalValue, step)
print(values2)

print(list(values2))
print(tuple(values2))

values3 = range(0, 9, 3)  # range(initialValue, finalValue, step)
print(values3)
print(list(values3))

values4 = list(range(9, 0, -1))  # builtin function
print(list(values4))

values4 = list(range(9, 0, -2))  # builtin function
print(list(values4))

values6 = range(0, 9, -1)  # range(initialValue, finalValue, step)
print(values6)
print(list(values6))

for i in range(9):
    # print(i, end='\n') # default 
    print(i, end=' ')

