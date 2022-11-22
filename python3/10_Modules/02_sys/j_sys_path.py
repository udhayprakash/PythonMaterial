#!/usr/bin/python3
"""
Purpose: sys.path
    - Gives the paths to refer
    Scope Resolution - LEGB
        - Builtin

"""
import sys

# print(sys.path) # gives a list of paths

for each_path in sys.path:
    print(each_path)

# NOTE: Installed modules are stored in "site-packages"


# def add(n1, n2):
#     return n1 + n2

# def sub(n1, n2):
#     return n1 - n2

# print(f"{add(2, 3) =}")
# print(f"{sub(2, 3) =}")

# Case 1 - importing script from current directory
import j_calculator

print(dir(j_calculator))

print(f"{j_calculator.add(2, 3) =}")
print(f"{j_calculator.sub(2, 3) =}")

# Case 1.1 - selective import
from j_calculator import add

assert j_calculator.add(2, 3) == add(2, 3)

# sub(2,3)  # NameError: name 'sub' is not defined. Did you mean: 'sum'?
print()

# Case 2
from myfolder import myops

print(dir(myops))

print(f"{myops.math.sqrt(81) =}")
print(f"{myops.factorial(8) =}")

# Case 2.1
from myfolder.myops import factorial

print(f"{factorial(8) =}")


# from asyncio_ex import a_asynchronous_function
# ModuleNotFoundError: No module named 'asyncio_ex'


sys.path.append(
    # absolute path
    # r"D:\MEGAsync\Python-related\PythonMaterial\python3\09_Iterators_generators_coroutines\05_asyncio_module"
    # relative path
    r"..\..\09_Iterators_generators_coroutines\05_asyncio_module"
)
print(f"{sys.path[-1] =}")


sys.dont_write_bytecode = True
# pycache files are not created when it is True


import a1_asynchronous_function as aaf  # Alias import

print(dir(aaf))

aaf.hello()

print(aaf.__doc__)
print()

print(f"{aaf.__file__ =}")
print(f"{__file__     =}")

print(f"{aaf.__name__ =}")
print(f"{aaf.__package__ =}")

# Assignments
# Try to add and use with relative path
# sys.path.insert(0, r'..\09_Iterators_Generators_Coroutines')
