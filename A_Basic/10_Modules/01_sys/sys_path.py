import sys

print type(sys.path)

# append custom path 
sys.path.insert(0, '/usr/bin/python')

for each in sys.path:
    print each


help(sys)

"""
api_version = 1013
    argv = ['sys_path.py']
    builtin_module_names = ('__builtin__', '__main__', '_ast', '_bisect', ...
    byteorder = 'little'
    copyright = 'Copyright (c) 2001-2018 Python Software Foundati...ematis...
    dllhandle = 1395720192L
    dont_write_bytecode = False
    exc_value = TypeError("<module 'sys' (built-in)> is a built-in module"...
    
    exec_prefix = r'C:\Python27'
    executable = r'C:\Python27\python.exe'
    
    flags = sys.flags(debug=0, py3k_warning=0, division_warn...unicode=0, ...
    float_info = sys.float_info(max=1.7976931348623157e+308, max_...epsilo...
    float_repr_style = 'short'
    hexversion = 34017264
    long_info = sys.long_info(bits_per_digit=30, sizeof_digit=4)
    
    maxint = 2147483647
    maxsize = 9223372036854775807L
    maxunicode = 65535
    
    meta_path = []
    modules = {'UserDict': <module 'UserDict' from 'C:\Python27\lib\UserDi...
    path = ['/usr/bin/python', r'C:\Users\udhayPrakash\Desktop\PythonMater...
    path_hooks = [<type 'zipimport.zipimporter'>]
    path_importer_cache = {'/usr/bin/python': <imp.NullImporter object>, r...
    
    platform = 'win32'
    
    prefix = r'C:\Python27'
    
    py3kwarning = False
    stderr = <open file '<stderr>', mode 'w'>
    stdin = <open file '<stdin>', mode 'r'>
    stdout = <open file '<stdout>', mode 'w'>
    
    subversion = ('CPython', '', '')
    
    version = '2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1...
    version_info = sys.version_info(major=2, minor=7, micro=15, releaselev...
    warnoptions = []
    
    winver = '2.7'

"""