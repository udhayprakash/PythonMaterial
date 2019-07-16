#!/usr/bin/python

'''
Purpose: creating a new CSV file

with - context manager

garbage collector -- java, python , ..
    - cpu clock cycle

'''

with open('sample.csv', 'w') as fh:
    fh.write('s_no,name,age,designation\n')
    fh.write('1,raghu,12,student\n')
    fh.write('2,praksh,87,retired professor\n')
    fh.close()