from shutil import *
import os
import time

def show_file_info(filename):
    stat_info = os.stat(filename)
    print '\tMode    :', stat_info.st_mode
    print '\tCreated :', time.ctime(stat_info.st_ctime)
    print '\tAccessed:', time.ctime(stat_info.st_atime)
    print '\tModified:', time.ctime(stat_info.st_mtime)

if not os.path.exists('example'):
    os.mkdir('example')

print 'SOURCE:'
show_file_info('shutil_copy2.py')

# copy2() works like copy(), but includes the access and modification times in the meta-data copied to the new file.
copy2('shutil_copy2.py', 'example')
print 'DEST:'


show_file_info('example/shutil_copy2.py')