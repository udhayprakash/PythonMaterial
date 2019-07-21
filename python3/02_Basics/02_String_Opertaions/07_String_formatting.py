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


print('''       
        Dear {customer}, 
                Your account ending with {accound_last_4_digits} was
                deducted {transaction_amount} on {transaction_time}.

        Thank you for shopping. Visit again!
         '''.format(
                 customer = 'Vijay Malya',
                 accound_last_4_digits = 1134,
                 transaction_amount = '20.5 crores',
                 transaction_time = '12th June 1947 12:34:45'
         ))

print("{:,}".format(1234567890.88))
print("{:_}".format(1234567890.88))