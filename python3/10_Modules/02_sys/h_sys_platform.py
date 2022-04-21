#!/usr/bin/python
"""
Purpose: sys module
"""
import sys

print('sys.platform', sys.platform)

if sys.platform == 'win32':
    print('you are in windows OS')
elif sys.platform == 'linux':
    print('you are in debian/ubuntu like OS')
elif sys.platform == 'linux2':
    print('you are in centos/redhat/fedora like OS')
elif sys.platform == 'darwin':
    print('you are in MAC like OS')
elif sys.platform == 'cygwin':
    print('you are in Windows/Cygwin OS')
