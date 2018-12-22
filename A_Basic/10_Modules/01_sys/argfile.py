# import time
# for i in range(90):
#     time.sleep(1)  # 1sec 
# name = raw_input('name=')
# print 'Entered named is', name


import sys

print __file__
print sys.argv

if len(sys.argv) < 2:
    print 'Enter name'
    print __file__, 'name'
    sys.exit(0)
    
name = sys.argv[1]
print 'Entered named is', name


