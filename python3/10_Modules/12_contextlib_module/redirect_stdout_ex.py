#!/usr/bin/python
"""
Purpose: redirect stdout within context
"""
import io
import sys
from contextlib import redirect_stdout

# Case 1
print('first statement')
with redirect_stdout(sys.stdout):
    print('second statement')

print('third statement')
print()

# Case 2
print('first statement')
with redirect_stdout(sys.stderr):
    print('second statement')

print('third statement')
print()


# Case 3 - writing to context
print('first statement')
f = io.StringIO()
with redirect_stdout(f):
    print('second statement')

print('third statement')
print(f'{f.getvalue() =}')
print()

# Case 4 - writing to file
print('first statement')
fh = open('result.txt', 'w')
with redirect_stdout(fh):
    print('second statement')

print('third statement')
