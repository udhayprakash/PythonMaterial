import sys
print('sys.base_exec_prefix =', sys.base_exec_prefix)
print('sys.base_prefix      =', sys.base_prefix)
print('sys.prefix           =', sys.prefix)
print('sys.exec_prefix      =', sys.exec_prefix)
print('sys.executable       =', sys.executable)

print('sys.byteorder             =', sys.byteorder)
# big    - big-endian    (most significant byte first) platforms
# little - little-endian (least significant byte first) platforms

print('sys.copyright        =', sys.copyright)
# print('sys._debugmallocstats() =', sys._debugmallocstats())

print('sys.dont_write_bytecode   =', sys.dont_write_bytecode)
# make this value to True , to stop creation of .pyc files on python file imports

print('sys.getdefaultencoding()   =', sys.getdefaultencoding())
print('sys.getfilesystemencoding()=', sys.getfilesystemencoding())
print('sys.getfilesystemencodeerrors()=', sys.getfilesystemencodeerrors())
print('sys.getswitchinterval()    =', sys.getswitchinterval())

num1 = 1234
print('sys.getrefcount(1234) =', sys.getrefcount(1234))
del num1
print('sys.getrefcount(1234) =', sys.getrefcount(1234))

for i in range(9999):
    print(sys.getrefcount(i), end=' ')

print()
for w in ["RandomJunkBlahBlah", "python", "version", "error", "Guido"]:
    print(w, sys.getrefcount(w))

num1 = 888888888888888888888
print('sys.sys.getsizeof(num1)=', sys.getsizeof(num1))
# Only the memory consumption directly attributed to the object 
# is accounted for, not the memory consumption of objects it refers 
# to.

print('sys.getwindowsversion()=', sys.getwindowsversion())
print('sys.hash_info             =', sys.hash_info)

print(hash(9))
print(hash(9.22))
print(hash(True))
print(hash(None))
print(hash((12, 2,3,23)))

# unhashables
# print(hash([12, 2,3,23]))
# print(hash({12, 2,3,23}))
# print(hash({'a':1, 'b':2}))
print(hash(frozenset({12, 23, 4})))


print('sys.hexversion             =', sys.hexversion)
print(hex(13))

print('sys.implementation         =', sys.implementation)
print('sys.int_info               =', sys.int_info)
print('sys.__interactivehook__()  =', sys.__interactivehook__())

print('sys.maxsize                =', sys.maxsize)
print('sys.maxunicode             =', sys.maxunicode)

print('sys.builtin_module_names   =', sys.builtin_module_names)
print('sys.modules                =')

from pprint import pprint 
pprint(sys.modules)


print('sys.version                =', sys.version)
print('sys.api_version            =', sys.api_version) # C API version for this interpreter
print('sys.version_info           =', sys.version_info)
print('sys.winver                 =', sys.winver) # version number used to form registry keys on Windows platforms

