#!/usr/bin/python

'''
file operations 
    - read  - r
    - write - w
    - append- a

    default is read mode
'''
fh = open('newfile.tsf', 'w')
fh.write('first line\n')

strings = ['first\n', 'second\n', 'third\n', 'fourth\n']
# for each_string in strings:
#     fh.write(each_string)
fh.writelines(strings)
fh.flush()
fh.close()

# assignment
# .writeline