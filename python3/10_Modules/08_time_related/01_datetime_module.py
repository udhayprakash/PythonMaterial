#!/usr/bin/python
"""
Purpose: datetime module
"""

import datetime

today = datetime.date.today()
print(today)                        # 2020-04-05
print('ctime  :', today.ctime())    # Sun Apr  5 00:00:00 2020
print('tuple  :', today.timetuple()) # time.struct_time(tm_year=2020,
#  tm_mon=4, tm_mday=5, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=6, 
# tm_yday=96, tm_isdst=-1)
print('Ordinal:', today.toordinal()) # 737520

print()
print('year  :', today.year)   # 2020
print('Month :', today.month)  # 4
print('Day   :', today.day)    # 5

'''
>>> datetime.time.min
datetime.time(0, 0)
>>> datetime.time.max
datetime.time(23, 59, 59, 999999)
>>> datetime.time.resolution
datetime.timedelta(microseconds=1)
>>>
>>>
>>> datetime.datetime.max
datetime.datetime(9999, 12, 31, 23, 59, 59, 999999)
>>> datetime.datetime.min
datetime.datetime(1, 1, 1, 0, 0)
>>> datetime.datetime.resolution
datetime.timedelta(microseconds=1)
>>>
>>>
>>> datetime.date.max
datetime.date(9999, 12, 31)
>>> datetime.date.min
datetime.date(1, 1, 1)
>>> datetime.date.resolution
datetime.timedelta(days=1)
'''