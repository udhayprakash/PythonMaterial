#!/usr/bin/python3
"""
Purpose: platform module
"""

import platform

print("platform.architecture()  :", platform.architecture())  # ('64bit', 'WindowsPE')
print("platform.machine()       :", platform.machine())  # AMD64
print("platform.system()        :", platform.system())  # Windows

print(f"{platform.python_revision()       = }")
print(f"{platform.python_implementation() = }")
print(f"{platform.python_revision()       = }")
print(f"{platform.python_version()        = }")
print(f"{platform.python_version_tuple() = }")
print()
print(f"{platform.uname()                = }")
print(f"{platform.version() = }")
print(f"{platform.win32_edition() = }")
print(f"{platform.win32_is_iot() = }")
print(f"{platform.win32_ver() = }")

print(dir(platform))
#
# ['_Processor', '_WIN32_CLIENT_RELEASES', '_WIN32_SERVER_RELEASES', '__builtins__', '__cached__', '__copyright__',
#  '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_comparable_version',
#  '_component_re', '_default_architecture', '_follow_symlinks', '_get_machine_win32', '_ironpython26_sys_version_parser',
#  '_ironpython_sys_version_parser', '_java_getprop', '_libc_search', '_mac_ver_xml', '_node', '_norm_version',
#  '_os_release_cache', '_os_release_candidates', '_os_release_line', '_os_release_unescape', '_parse_os_release',
#  '_platform', '_platform_cache', '_pypy_sys_version_parser', '_sys_version', '_sys_version_cache',
#  '_sys_version_parser', '_syscmd_file', '_syscmd_ver', '_uname_cache', '_unknown_as_blank', '_ver_output',
#  '_ver_stages', 'architecture', 'collections', 'freedesktop_os_release', 'functools', 'itertools', 'java_ver',
#  'libc_ver', 'mac_ver', 'machine', 'node', 'os', 'platform', 'processor', 'python_branch', 'python_build',
#  'python_compiler', 'python_implementation', 'python_revision', 'python_version', 'python_version_tuple', 're',
#  'release', 'subprocess', 'sys', 'system', 'system_alias', 'uname', 'uname_result', 'version', 'win32_edition',
#  'win32_is_iot', 'win32_ver']
