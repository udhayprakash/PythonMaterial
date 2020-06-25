#!/usr/bin/python
"""
Purpose: platform module
"""

import platform

print("platform.architecture()  :", platform.architecture())  # ('64bit', 'WindowsPE')
print("platform.machine()       :", platform.machine())  # AMD64
print("platform.system()        :", platform.system())  # Windows

print(dir(platform))