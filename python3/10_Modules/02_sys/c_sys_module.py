#!/usr/bin/python
"""
Purpose: sys module 
"""
import sys 

print(f''' 
    {sys.executable      =}
    {sys.exec_prefix     =}

    {sys.prefix          =}
    {sys.base_prefix     =}
    {sys.base_exec_prefix=}
    {sys.pycache_prefix  =}
 
    {sys.dont_write_bytecode=}

    {sys.getallocatedblocks()       =}
    {sys.getcheckinterval()         =}
    {sys.getdefaultencoding()       =}
    {sys.getfilesystemencodeerrors()=}
    {sys.getfilesystemencoding()    =}
    {sys.getprofile()               =}
    {sys.getswitchinterval()        =}

    {sys.setcheckinterval           =}
    {sys.setprofile                 =}
    {sys.setswitchinterval          =}

    {sys.flags                      =}
    {sys.exc_info()                 =}

    {sys.getrecursionlimit()        =}
    {sys.setrecursionlimit          =}

''')

# NOTE: when using virtualenvironment
# then prefix and base_prefix will change

# bytecode files -.pyc(in python 2.x) & __pycache__ folder

# sys.exc_info - exc_type, exc_value, exc_traceback

try:
    raise ValueError('Incorrect value')
except  ValueError:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print(f'{sys.exc_info() =}')
    print(exc_type, exc_value, exc_traceback)