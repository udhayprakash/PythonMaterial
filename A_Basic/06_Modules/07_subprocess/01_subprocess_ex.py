from subprocess import call, Popen
from sys import platform, exit
import os

# subprocess.Popen is more general than subprocess.call.
# Popen doesn't block, allowing you to interact with the 
# process while it's running, or continue with other things 
# in your Python program; whereas call does block.

if platform in ['linux', 'linux2', 'darwin']:
    os.system('ls -l /usr/bin/python')
    call('ls -l /usr/bin/python', shell=True)
    result = Popen('ls -l /usr/bin/python', shell=True)
    print 'result==============\n', result
elif platform == 'win32':
    print os.system('dir /x C:\Python27')
    print call('dir /x C:\Python27', shell=True)
    result = Popen('dir /x C:\Python27', shell=True)
    print 'result==============\n', result
else:
    print "unhandled platform :", platform
    exit(1)
