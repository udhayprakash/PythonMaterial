from shutil import *
from subprocess import *
import os

'''
By default when a new file is created under Unix,
it receives permissions based on the umask of the current user.
To copy the permissions from one file to another, use copymode().
'''

f = open('file_to_change.txt', 'wt')
f.write('content')
f.close()
os.chmod('file_to_change.txt', 0o444)

print('BEFORE:', getstatus('file_to_change.txt'))
copymode('shutil_copymode.py', 'file_to_change.txt')
print('AFTER :', getstatus('file_to_change.txt'))
