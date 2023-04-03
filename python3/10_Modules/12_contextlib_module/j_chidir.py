""""
Purpose:
    contextlib.chdir
    introduced in python 3.11
"""

import contextlib
import os

print("BEFORE Current directory:", os.getcwd())

with contextlib.chdir("..") as cwd:
    print("INSIDE Current directory:", os.getcwd())

print("AFTER  Current directory:", os.getcwd())
