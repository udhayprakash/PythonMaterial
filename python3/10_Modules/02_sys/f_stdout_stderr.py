#!/usr/bin/python3
"""
Purpose: sys module
"""
import sys

print(f'''
    {sys.stderr =}
    {sys.stdin  =}
    {sys.stdout =}
''')

sys.stdout.write('Hello world\n')
print('Hello world', end='\n')

sys.stderr.write('Hello world Error\n')
# raise ValueError('wrong error')

# sys.stdin.read() is similar to input()
