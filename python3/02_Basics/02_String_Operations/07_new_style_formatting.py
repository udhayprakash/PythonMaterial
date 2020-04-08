#!/usr/bin/python
"""
Purpose: String formatting
        NEW STYLE string formatting
"""
print('' % ())
print('{}'.format(''))

print('{} and {}'.format('cat', 'mouse'))
print('{} and {}'.format(213, 'mouse'))
print('{} and {}'.format(213.0, True))
print('{} and {}'.format(None, True))

print()
print("{}".format(1234567890.88))  # 1234567890.88
print("{:,}".format(1234567890.88))  # 1,234,567,890.88
print("{:_}".format(1234567890.88))  # 1_234_567_890.88
print()

print('{}'.format(1024), 1024)  # 1024 1024
print('{:b}'.format(1024), bin(1024))  # 10000000000 0b1000000000
print('{:o}'.format(1024), oct(1024))  # 2000 0o2000
print('{:x}'.format(1024), hex(1024))  # 400 0x400
print()

import math

print('math.pi', math.pi)  # 3.141592653589793
print('{}'.format(math.pi))  # 3.141592653589793
# print('{:d}'.format(math.pi))
print('{:f}'.format(math.pi))  # 3.141593
print('{:F}'.format(math.pi))  # 3.141593
print('{:g}'.format(math.pi))  # 3.14159
print()

print('Name:{} Age:{} Salary:{}'.format('udhay', 99, 9999.9999))
print('''Name  :{}
         Age   :{}
         Salary:{}'''.format('udhay', 99, 9999.9999))

print('''Name  :{0} Name  :{0} Salary:{2}
         Age   :{1} Name  :{0}
         Salary:{2}'''.format('udhay', 99, 9999.9999))
#                               0      1     2

print('''Name  :{2} Name  :{2} Salary:{2}
         Age   :{2} Name  :{2}
         Salary:{2}'''.format('udhay', 99, 9999.9999))
#                               0      1     2

print('''Name  :{NAME} Name  :{NAME} Salary:{SALARY}
         Age   :{AGE} Name  :{NAME}
         Salary:{SALARY}'''.format(NAME='udhay',
                                   AGE=99, SALARY=9999.9999))

# ------------------------------------------------------------
# Method 1
print('''
        Dear {customer},
                Your account ending with {accound_last_4_digits} was
                deducted {transaction_amount} on {transaction_time}.

        Thank you for shopping. Visit again!!!
         '''.format(
    customer='Vijay Malya',
    accound_last_4_digits=1134,
    transaction_amount='20.5 crores',
    transaction_time='12th June 1947 12:34:45'
))

# Method 2
result = {
    'customer': 'Vijay Malya',
    'accound_last_4_digits': 1134,
    'transaction_amount': '20.5 crores',
    'transaction_time': '12th June 1947 12:34:45'
}

print('''
        Dear {customer},
                Your account ending with {accound_last_4_digits} was
                deducted {transaction_amount} on {transaction_time}.

        Thank you for shopping. Visit again!
         '''.format(
    **result
))

# Method 3
print('''
        Dear {customer},
                Your account ending with {accound_last_4_digits} was
                deducted {transaction_amount} on {transaction_time}.

        Thank you for shopping. Visit again!
         '''.format_map(
    result
))
