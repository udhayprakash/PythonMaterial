#!/usr/bin/python
"""
purpose: sys.plaform
"""

print('sys.plaform', sys.plaform)

if sys.plaform == 'win32':
    print('you are in windows OS')
elif sys.plaform == 'linux':
    print('you are in debian/ubuntu like OS')
elif sys.plaform == 'linux2':
    print('you are in centos/redhat/fedora like OS')
elif sys.plaform == 'darwin':
    print('you are in MAC like OS')