#!/usr/bin/python
"""
Purpose: Loops
    break     - breaks the complete loop
    continue  - skip the current loop
    pass      - will do nothing. it is like a todo
    sys.exit  - will exit the script execution

"""
i = 0
while i <= 7:
    i += 1
    print(i, end = ' ')

print('\n importance of break')
i = 0
while i <= 7:
    i += 1
    if i == 5:
        break
    print(i, end = ' ')


print('\n importance of continue')
i = 0
while i <= 7:
    i += 1
    if i == 5:
        continue
    print(i, end = ' ')

print('\n importance of pass')
i = 0
while i <= 7:
    i += 1
    if i == 5:
        pass  # It acts as a placeholder
    print(i, end = ' ')

import sys

print('\nimportance of sys.exit')
i = 0
while i < 7:
    i += 1
    if i == 5:
        sys.exit(0)
    print(i, end = ' ')
# exit code 0 - successful/normal termination
# exit code non-zero - abnormal termination
print('next statement')

