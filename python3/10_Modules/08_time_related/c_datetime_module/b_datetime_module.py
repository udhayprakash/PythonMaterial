#!/usr/bin/python
"""
Purpose: datetime.date
"""

import datetime

today = datetime.date.today()
print(today)  # 2020-06-24
print("ctime  :", today.ctime())  # Wed Jun 24 00:00:00 2020
print("tuple  :", today.timetuple())
# time.struct_time(tm_year=2020, tm_mon=6, tm_mday=24, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=2, tm_yday=176, tm_isdst=-1)

print("Ordinal:", today.toordinal())  # 737600

print()
print("year  :", today.year)  # 2020
print("Month :", today.month)  # 6
print("Day   :", today.day)  # 24
