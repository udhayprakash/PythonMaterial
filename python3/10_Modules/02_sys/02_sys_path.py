#!/usr/bin/python
"""
Purpose:

    Python scoping :- LEGB
"""
import sys

# print(type(sys.path))

# append custom path 
# sys.path.insert(0, '/usr/bin/python')
sys.path.insert(0, r'C:\Users\udhayPrakash\Desktop\PythonMaterial\python3\07_Functions')  # 001_simple_function.py

for each in sys.path:
    print(each)

# from a001_simple_function import hello
# hello()