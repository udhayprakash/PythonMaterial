#!/usr/bin/python
"""
Purpose: Calculating the average for the
    inputted numbers in run-time
"""


total = 0
count = 0
while True:
    try:
        inp = eval(input('Enter a number: '))
    except:
        break
    value = float(inp)
    total += value
    count += 1

average = total / count
print('Average:', average)
