#!/usr/bin/python
"""
Purpose: time module
"""
import time
print(f'{time.altzone  =}')  # -23400
print(f'{time.daylight =}')  # 0 or 1
print(f'{time.timezone   =}')  # -19800  - second difference from GMtime
print(f'{time.tzname   =}')  # ('India Standard Time', 'India Daylight Time')
print()

# print(f'{time.gmtime()  =}')
# time.struct_time(tm_year=2020, tm_mon=6, tm_mday=24, tm_hour=3, tm_min=53, tm_sec=15, tm_wday=2, tm_yday=176, tm_isdst=0)
# print(f'{time.localtime()  =}')
# time.struct_time(tm_year=2020, tm_mon=6, tm_mday=24, tm_hour=9, tm_min=23, tm_sec=15, tm_wday=2, tm_yday=176, tm_isdst=0)
print(f'{time.gmtime(23434)            =}')
print(f'{time.localtime(23434)         =}')

print(f'{time.asctime(time.gmtime())   =}')   # 'Wed Jun 24 15:41:07 2020'
print(f'{time.asctime(time.localtime())=}')   # 'Wed Jun 24 21:11:07 2020'
print(f'{time.asctime()                =}')   # 'Wed Jun 24 21:11:07 2020'
print()

print(f'{time.ctime()                  =}')   # 'Wed Jun 24 21:11:07 2020'
print(f'{time.ctime(1000)              =}')   # 'Thu Jan  1 05:46:40 1970'
print(f'{time.ctime(900009000)         =}')   # 'Fri Jul 10 00:00:00 1998'
print()

print(f'{time.time()     =}')  # 1592971057.277388 - epoch time (no. of second from Jan 1st, 1970)
print(f'{time.time_ns()  =}')  # 1592971057277388100 epoch time in nano seconds
