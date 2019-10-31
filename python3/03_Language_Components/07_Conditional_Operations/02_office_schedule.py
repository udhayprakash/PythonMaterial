#!/usr/bin/python
"""
Purpose:
    Monday to Friday  : - 9 am to 6 pm
    Saturday          : - 9 am to 1 pm
    Sunday            : - Holiday
"""
__author__ = 'Python Tutor'

week_of_day = input('Enter week of day:').lower().strip()

########## METHOD 1
if week_of_day == 'monday':
    print('TIMINGS: 9 am to 6 pm')
elif week_of_day == 'tuesday':
    print('TIMINGS: 9 am to 6 pm')
elif week_of_day == 'wednesday':
    print('TIMINGS: 9 am to 6 pm')
elif week_of_day == 'thursday':
    print('TIMINGS: 9 am to 6 pm')
elif week_of_day == 'friday':
    print('TIMINGS: 9 am to 6 pm')
elif week_of_day == 'saturday':
    print('TIMINGS: 9 am to 1 pm')
elif week_of_day == 'sunday':
    print(' --HOLIDAY ---')
else:
    print('Invalid input!!')


########## METHOD 2
if (week_of_day == 'monday' or 
    week_of_day == 'tuesday' or
    week_of_day == 'wednesday' or 
    week_of_day == 'thursday' or 
    week_of_day == 'friday'):
    print('TIMINGS: 9 am to 6 pm')
elif week_of_day == 'saturday':
    print('TIMINGS: 9 am to 1 pm')
elif week_of_day == 'sunday':
    print(' --HOLIDAY ---')
else:
    print('Invalid input!!')

########## METHOD 3
# in - membership check operator
if week_of_day in ( 'monday','tuesday','wednesday', 'thursday', 'friday'):
    print('TIMINGS: 9 am to 6 pm')
elif week_of_day == 'saturday':
    print('TIMINGS: 9 am to 1 pm')
elif week_of_day == 'sunday':
    print(' --HOLIDAY ---')
else:
    print('Invalid input!!')