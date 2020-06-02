#!/usr/bin/python
"""
Purpose: sysconfig module 
    Ref: https://docs.python.org/3.8/library/sysconfig.html

    In terminal, 
        python -m sysconfig
"""
import sysconfig


print(f'{sysconfig.is_python_build()    =}')    # False
# Return True if the running Python interpreter was built from source 

print(f'{sysconfig.get_platform()       =}')    # 'win-amd64'

print(f'{sysconfig.get_python_version() =}')
print(f'{sysconfig.get_scheme_names()   =}')
print(f'{sysconfig.get_paths()          =}')
print(f'{sysconfig.get_path_names()     =}')
# print(f'{sysconfig.get_path()           =}')
print(f'{sysconfig.get_config_vars()    =}')
# print(f'{sysconfig.get_config_var()     =}')
# get_config_h_filename
# get_makefile_filename
# parse_config_h

'''
>>> sysconfig.get_config_var('Py_ENABLE_SHARED')
0
>>> sysconfig.get_config_var('LIBDIR')
'/usr/local/lib'
>>> sysconfig.get_config_vars('AR', 'CXX')
['ar', 'g++']

'''