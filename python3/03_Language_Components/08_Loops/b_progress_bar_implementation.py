#!/usr/bin/python
"""
Purpose: Progress Status Bar Implementation

    Escape Sequences
        \t - tab space
        \n - new line
        \r - rare feed
"""


print('Udhay Prakash')
print('Udhay\tPrakash')
print('Udhay\nPrakash')
print()

print('Udhay\rPrakash')
print('Prakash\rUdhay')

print('1234567890\rDOG')

data = list(range(-100, 10_00_000, 3))
data_length = len(data)

for loop_index, number in enumerate(data):
    # print(loop_index, data_length, round(loop_index/ data_length, 2) * 100)
    completed_percentage = round((loop_index / data_length) * 100, 2)
    print(f'\r{completed_percentage: 5} % completed', end=' ')

"""
Assignment: Progress bar implementation

[*         ]  10
[**        ]  20
[***       ]  30
[****      ]  40
[*****     ]  50
[******    ]  60
[*******   ]  70
[********  ]  80
[********* ]  90
[**********] 100
"""