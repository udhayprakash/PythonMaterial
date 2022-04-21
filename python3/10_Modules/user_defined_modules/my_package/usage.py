#!/usr/bin/python
"""
Purpose: importing and using remote file
"""
import sys

sys.path.insert(
    0,
    r"D:\MEGAsync\Python-related\training\python_related\python_batch154\07_Functions",
)
from fibonacci_series import fib

print(f"{fib(9) =}")
