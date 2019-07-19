#!/usr/bin/python
"""
Purpose:
    Monday to Friday  : - 9 am to 6 pm
    Saturday          : - 9 am to 1 pm
    Sunday            : - Holiday
"""
__author__ = 'Python Tutor'

day_of_week = input('Enter day of week:').lower().strip()
print(f'you entered {day_of_week}')

if day_of_week == 'monday':
    print('Timings: 9 am to 6 pm')
elif day_of_week == 'tuesday':
    print('Timings: 9 am to 6 pm')
elif day_of_week == 'wednesday':
    print('Timings: 9 am to 6 pm')
elif day_of_week == 'thursday':
    print('Timings: 9 am to 6 pm')
elif day_of_week == 'friday':
    print('Timings: 9 am to 6 pm')
elif day_of_week == 'saturday':
    print('Timings: 9 am to 1 pm')
elif day_of_week == 'sunday':
    print('TODAY IS HOLIDAY')
else:
    print('Invalid entry')


if (
    (day_of_week == 'monday') or 
    (day_of_week == 'tuesday') or 
    (day_of_week == 'wednesday') or
    (day_of_week == 'thursday')  or 
    (day_of_week == 'friday')
    ):
    print('Timings: 9 am to 6 pm')
elif day_of_week == 'saturday':
    print('Timings: 9 am to 1 pm')
elif day_of_week == 'sunday':
    print('TODAY IS HOLIDAY')
else:
    print('Invalid entry')


if day_of_week in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday'):
    print('Timings: 9 am to 1 pm')
elif day_of_week == 'saturday':
    print('Timings: 9 am to 1 pm')
elif day_of_week == 'sunday':
    print('TODAY IS HOLIDAY')
else:
    print('Invalid entry')