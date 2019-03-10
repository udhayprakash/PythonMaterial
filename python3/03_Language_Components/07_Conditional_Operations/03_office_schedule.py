#!/usr/bin/python
"""
Purpose:
    Monday to Friday  : - 9 am to 6 pm
    Saturday          : - 9 am to 1 pm
    Sunday            : - Holiday
"""
__author__ = 'Python Tutor'

day_of_the_week = input('Enter the day of the week:').lower().strip()
print("day_of_the_week:", day_of_the_week, type(day_of_the_week))

if (day_of_the_week == 'monday'
        or day_of_the_week == 'tuesday'
        or day_of_the_week == 'wednesday'
        or day_of_the_week == 'thursday'
        or day_of_the_week == 'friday'):

    print("Office Timings: 9 am to 6 pm")

elif day_of_the_week == 'saturday':
    print("Office Timings: 9 am to 1 pm")
elif day_of_the_week == 'sunday':
    print("SUNDAY is HOLIDAY!!!!!!")
# else:
#     print("Please enter the correct weekname!")

# in operator - membership check operator

if day_of_the_week in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday'):
    print("Office Timings: 9 am to 6 pm")
elif day_of_the_week == 'saturday':
    print("Office Timings: 9 am to 1 pm")
elif day_of_the_week == 'sunday':
    print("SUNDAY is HOLIDAY!!!!!!")
else:
    print("Please enter the correct weekname!")
