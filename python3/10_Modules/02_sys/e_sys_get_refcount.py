#!/usr/bin/python
"""
Purpose: sys module 
"""
import sys 

num1 = 123
num2 = 123
num3 = 23

print(f'{sys.getrefcount(123) =}')
# NOTE: Returns how many variables are refering 
# to this value
# Every number will have atleast 2 references

for i in range(1000):
    print(f'{i} {sys.getrefcount(i)}')

print(f'{sys.getrefcount(-0.2) =}')
print(f'{sys.getrefcount(None) =}')
print(f'{sys.getrefcount(1)    =}')
print(f'{sys.getrefcount(True) =}')
print(f'{sys.getrefcount(0)    =}')
print(f'{sys.getrefcount(False)=}')

