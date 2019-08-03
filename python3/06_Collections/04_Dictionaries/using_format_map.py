#!/usr/bin/python
"""
Purpose: format , format with dict unpacking and format_map
"""


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


result = {
        'customer' : 'Vijay Malya',
        'accound_last_4_digits' : 1134,
        'transaction_amount' : '20.5 crores',
        'transaction_time' : '12th June 1947 12:34:45'
}

# Dictionary Unpacking
print('''       
        Dear {customer}, 
                Your account ending with {accound_last_4_digits} was
                deducted {transaction_amount} on {transaction_time}.

        Thank you for shopping. Visit again!
         '''.format(
                 **result
         ))


# Using format_map
print('''       
        Dear {customer}, 
                Your account ending with {accound_last_4_digits} was
                deducted {transaction_amount} on {transaction_time}.

        Thank you for shopping. Visit again!
         '''.format_map(
                 result
         ))