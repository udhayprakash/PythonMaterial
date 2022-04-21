#!/usr/bin/python
"""
Purpose: sysconfig module
    Ref: https://docs.python.org/3.8/library/sysconfig.html

    In terminal,
        python -m sysconfig
"""
import sysconfig
from pprint import pprint

# print(dir(sysconfig))

print(f"{sysconfig.is_python_build()    =}")  # False
# Return True if the running Python interpreter was built from source

print(f"{sysconfig.get_platform()       =}")  # 'win-amd64'

print(f"{sysconfig.get_python_version() =}")  # '3.8'
print(f"{sysconfig.get_scheme_names()   =}")
# ('nt', 'nt_user', 'osx_framework_user', 'posix_home', 'posix_prefix', 'posix_user')

print(f"{sysconfig.get_path_names()     =}")
# ('stdlib', 'platstdlib', 'purelib', 'platlib', 'include', 'scripts', 'data')

print("sysconfig.get_paths()\n")
pprint(sysconfig.get_paths())


print("sysconfig.get_config_vars()\n")
pprint(sysconfig.get_config_vars())
# get_config_h_filename
# get_makefile_filename
# parse_config_h

"""
>>> sysconfig.get_config_var('Py_ENABLE_SHARED')
0
>>> sysconfig.get_config_var('LIBDIR')
'/usr/local/lib'
>>> sysconfig.get_config_vars('AR', 'CXX')
['ar', 'g++']

"""
