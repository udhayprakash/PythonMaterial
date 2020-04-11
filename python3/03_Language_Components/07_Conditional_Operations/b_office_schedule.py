#!/usr/bin/python
"""
Purpose: Office Schedule
    Monday to Friday  :- 9 am to 6 pm
    Saturday          :- 9 am to 1 pm
    Sunday            :- Holiday

"""
__name__ = 'Author'

# week_of_day = 'Monday'
week_of_day = input('Enter week of day:').title().strip()

# Method  1
if week_of_day == 'Monday':
    print('TIMINGS: 9 AM to 6 PM')
elif week_of_day == 'Tuesday':
    print('TIMINGS: 9 AM to 6 PM')
elif week_of_day == 'Wednesday':
    print('TIMINGS: 9 AM to 6 PM')
elif week_of_day == 'Thursday':
    print('TIMINGS: 9 AM to 6 PM')
elif week_of_day == 'Friday':
    print('TIMINGS: 9 AM to 6 PM')
elif week_of_day == 'Saturday':
    print('TIMINGS: 9 AM to 1 PM')
elif week_of_day == 'Sunday':
    print('----HOLIDAY----------')
else:
    print('INVALID ENTRY! PLEASE TRY AGAIN!!')

# Method 2 ----------------------------------------
if (week_of_day == 'Monday' or
        week_of_day == 'Tuesday' or
        week_of_day == 'Wednesday' or
        week_of_day == 'Thursday' or
        week_of_day == 'Friday'):  # 5 + 4 = 9 operations
    print('TIMINGS: 9 AM to 6 PM')
elif week_of_day == 'Saturday':
    print('TIMINGS: 9 AM to 1 PM')
elif week_of_day == 'Sunday':
    print('----HOLIDAY----------')
else:
    print('INVALID ENTRY! PLEASE TRY AGAIN!!')

# Method 3 ----------------------------------------
# in - membership check operator
# in operator works with any iterable object
if week_of_day in ['Monday', 'Tuesday', 'Wednesday',
                   'Thursday', 'Friday']:
    print('TIMINGS: 9 AM to 6 PM')
elif week_of_day == 'Saturday':
    print('TIMINGS: 9 AM to 1 PM')
elif week_of_day == 'Sunday':
    print('----HOLIDAY----------')
else:
    print('INVALID ENTRY! PLEASE TRY AGAIN!!')
