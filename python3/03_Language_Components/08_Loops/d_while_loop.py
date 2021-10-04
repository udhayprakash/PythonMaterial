#!/usr/bin/python3
"""
Purpose: while loop
    SYNTAX:
        initialization
        while loop- condition
            logic
            increment/decrement

NOTE: i++, i--, --i, ++i (unary operations) are not supported in python
"""
print('\nincrementing loop with increment first')

i = 0                       # initialization
while i < 5:                # condition
    i += 1                  # increment/decrement
    print(i, end= ' ')      # Logic
print()

print('\nincrementing loop with increment last')
i = 0
while i < 5:           # condition - less than
    print(i, end=' ')  # logic
    i += 1             # increment/decrement
print()


i = 0
while i <= 5:          # condition - less than or equal
    print(i, end=' ')  # logic
    i += 1             # increment/decrement
print()


# ------------
print('\n\ndecrementing loop with decrement first')
j = 5
while j > 0:
    j -= 1
    print(j, end=' ')
print()

print('\n\ndecrementing loop with decrement last')
j = 5
while j > 0:           # condition- greater than
    print(j, end=' ')
    j -= 1
print()


j = 5
while j >= 0:         # condition- greater than or equal
    print(j, end=' ')
    j -= 1
