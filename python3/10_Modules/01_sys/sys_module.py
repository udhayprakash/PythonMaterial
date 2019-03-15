
import sys

print('sys.version', sys.version)
print('sys.version_info', sys.version_info)
print('sys.executable', sys.executable)
print('sys.platform', sys.platform)
'''
windows - win32 
Redhat/cent os/fedora - linux2
debian/ubuntu, ///    - linux
mac os                - darwin 
'''
print('sys.getrecursionlimit()', sys.getrecursionlimit())
for i in (sys.stdin, sys.stdout, sys.stderr):
    print(i)

print('Hello world!')
sys.stdout.write('Hello world!\n')
# sys.modules.keys()


print('sys.path', type(sys.path))

for each_path in sys.path:
    print(each_path)

# import udhay
user_input = sys.stdin.readline()
print("Input : " + user_input)


print('sys.copyright', sys.copyright)


# This python sys module method returns the count for references to an object where it is used. Python keeps track of this value, as, when this value reaches 0 in a program, the memory for this variable is cleaned up. 
print('sys.getrefcount(0)', sys.getrefcount(0))
name = 'Udhay'
print('sys.getrefcount(name)', sys.getrefcount(name))
print('sys.getrefcount(None)', sys.getrefcount(None))


