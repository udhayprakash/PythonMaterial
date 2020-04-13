#!/usr/bin/python
"""
Purpose: Loops
    break     - breaks the complete loop
    continue  - skip the current loop
    pass      - will do nothing. it is like a todo
    sys.exit  - will exit the script execution

"""
__name__ = 'Author'
i = 0
while i <= 7:
    i += 1
    print(i)

print('\n importance of break')
i = 0
while i <= 7:
    i += 1
    if i == 5:
        break
    print(i)

print('\n importance of continue')
i = 0
while i <= 7:
    i += 1
    if i == 5:
        continue
    print(i)

print('\n importance of pass')
i = 0
while i <= 7:
    i += 1
    if i == 5:
        pass  # It acts as a placeholder
    print(i)

import sys

print('importance of sys.exit')
i = 0
while i < 7:
    i += 1
    if i == 5:
        sys.exit(0)
    print(i)
# exit code 0 - successful/normal termination
# exit code non-zero - abnormal termination
print('next statement')



