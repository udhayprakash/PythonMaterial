from shutil import *
import os
import time

"""
To copy other meta-data about the file (permissions, last access time, and last modified time), use copystat().
"""

def show_file_info(filename):
    stat_info = os.stat(filename)
    print('\tMode    :', stat_info.st_mode)
    print('\tCreated :', time.ctime(stat_info.st_ctime))
    print('\tAccessed:', time.ctime(stat_info.st_atime))
    print('\tModified:', time.ctime(stat_info.st_mtime))

f = open('file_to_change.txt', 'wt')
f.write('content')
f.close()
os.chmod('file_to_change.txt', 0o444)

print('BEFORE:')
show_file_info('file_to_change.txt')
copystat('shutil_copystat.py', 'file_to_change.txt')
print('AFTER :')
show_file_info('file_to_change.txt')
