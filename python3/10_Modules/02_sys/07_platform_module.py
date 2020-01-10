#!/usr/bin/python
"""
Purpose:
"""

import platform

print("platform.architecture()  :", platform.architecture())  # ('64bit', 'WindowsPE')
print("platform.machine()       :", platform.machine())  # AMD64
print("platform.system()        :", platform.system())  # Windows
