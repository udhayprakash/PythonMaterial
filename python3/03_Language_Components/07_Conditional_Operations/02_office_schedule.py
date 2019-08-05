#!/usr/bin/python
"""
Purpose:
    Monday to Friday  : - 9 am to 6 pm
    Saturday          : - 9 am to 1 pm
    Sunday            : - Holiday
"""
__author__ = 'Python Tutor'

day_of_week = input('Enter day of week: ').lower().strip()
print(day_of_week)

if day_of_week == 'monday':
    print('TIMING: - 9 am to 6 pm')
elif day_of_week == 'tuesday':
    print('TIMING: - 9 am to 6 pm')
elif day_of_week == 'wednesday':
    print('TIMING: - 9 am to 6 pm')
elif day_of_week == 'thursday':
    print('TIMING: - 9 am to 6 pm')
elif day_of_week == 'friday':
    print('TIMING: - 9 am to 6 pm')
elif day_of_week == 'saturday':
    print('TIMING: - 9 am to 1 pm')
elif day_of_week == 'sunday':
    print('HOLIDAY')
else:
    print('Invalid input!!!!')


if (day_of_week == 'monday' or 
    day_of_week == 'tuesday' or 
    day_of_week == 'wednesday' or 
    day_of_week == 'thursday' or 
    day_of_week == 'friday' ):
    print('TIMING: - 9 am to 6 pm')
elif day_of_week == 'saturday':
    print('TIMING: - 9 am to 1 pm')
elif day_of_week == 'sunday':
    print('HOLIDAY')
else:
    print('Invalid input!!!!') 

# in - membership check
if day_of_week in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday'):
   print('TIMING: - 9 am to 6 pm')
elif day_of_week == 'saturday':
    print('TIMING: - 9 am to 1 pm')
elif day_of_week == 'sunday':
    print('HOLIDAY')
else:
    print('Invalid input!!!!') 