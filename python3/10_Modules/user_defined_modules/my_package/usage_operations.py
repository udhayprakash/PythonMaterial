#!/usr/bin/python
"""
Purpose: Script for usage of operations.py
"""
import sys

# Below flag should be placed first, before importing modules
sys.dont_write_bytecode = True

import operations

print(f"{operations.fibonacci(9) =}")
print(f"{operations.factorial(9) =}")
print()


# selective import
from operations import fibonacci

print(f"{fibonacci(9) =}")
print()


# wildcard import
from operations import *

print(f"{fibonacci(9) =}")
print(f"{factorial(9) =}")


# byte code (.pyc) file created can be stopped, by setting
# environment variable
# export PYTHONDONTWRITEBYTECODE=1
