#!/usr/bin/python
"""
Purpose: String formatting
        NEW STYLE string formatting
"""

print('{}'.format(''))
print('{} and {}'.format('cat', 'mouse'))

print('Name:{} Age:{} Salary:{}'.format('udhay', 99, 9999.9999))

print('''Name  :{} 
         Age   :{} 
         Salary:{}'''.format('udhay', 99, 9999.9999))

print('My Name: {0}. My Name: {0}. My Name: {0}. My Name: {0}. '.format('udhay', 23, 34234))

print('''
        Name  :{2} 
        Age   :{0} 
        Salary:{0}'''.format('udhay', 99, 9999.9999))

print('''
        Name  :{NAME} , Name  :{NAME}
        Age   :{AGE} 
        Salary:{SALARY}'''.format(NAME='udhay', AGE=99, SALARY=9999.9999))