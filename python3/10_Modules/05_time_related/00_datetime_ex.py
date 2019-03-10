#!/usr/bin/python
"""
Purpose: datetime module demonstration
"""
import datetime

print(dir(datetime))

print('datetime.MAXYEAR:', datetime.MAXYEAR)
print('datetime.MINYEAR:', datetime.MINYEAR)

print('datetime.tzinfo:', datetime.tzinfo)
"""
datetime  has three different kinds of objects:
    1. date object      :- stores the date 
    2. time object      :- stores the time 
    3. datetime object  :- stores both the date and time 
"""

now = datetime.datetime.now()
print('now                      :', now)
print('type(now)                :', type(now))

today = now.date()
print('today                    :', today)
print('type(today)              :', type(today))

moment = now.time()
print('moment                   :', moment)
print('type(moment)             :', type(moment))

now_using_combine = datetime.datetime.combine(today, moment)
print('now_using_combine        :', moment)
print('type(now_using_combine)  :', type(moment))

print()
yesterday = today - datetime.timedelta(1)
print('yesterday                :', yesterday)
print('type(yesterday)          :', type(yesterday))

# Getting the difference between two datetime objects
time_difference = yesterday - today
print('time_difference          :', time_difference)
print('type(time_difference)    :', type(time_difference))

print()
# date object has three mandatory arguments
my_date = datetime.date(1947, 8, 15)  # order YEAR, MONTH, DAY
print('my_date                  :', my_date)
print('type(my_date)            :', type(my_date))

my_date = datetime.date(day=15, year=1947, month=8)  # order can be changed using keyword args
print('my_date                  :', my_date)
print('type(my_date)            :', type(my_date))

print()
# time object don't have mandatory arguments
my_time = datetime.time()
print('my_time                  :', my_time)
print('type(my_time)            :', type(my_time))

my_time = datetime.time(0, 0)  # first argument hour, second minute
print('my_time                  :', my_time)
print('type(my_time)            :', type(my_time))

my_time = datetime.time(hour=0, minute=0)
print('my_time                  :', my_time)
print('type(my_time)            :', type(my_time))

print()
# datetime objects have the same mandatory arguments as date object
my_datetime = datetime.datetime(year=1984, month=6, day=24)  # Time is set to 0:00
print('my_datetime              :', my_datetime)
print('type(my_datetime)        :', type(my_datetime))

my_datetime = datetime.datetime(1984, 6, 24, 18, 30)
print('my_datetime              :', my_datetime)
print('type(my_datetime)        :', type(my_datetime))

my_datetime = datetime.datetime(year=1984, month=6, day=24, hour=18, minute=30)
print('my_datetime              :', my_datetime)
print('type(my_datetime)        :', type(my_datetime))

# Change one datetime object to obtain another using the replace method
another_datetime = my_datetime.replace(year=2019, month=1)
print('another_datetime         :', another_datetime)
print('type(another_datetime)   :', type(another_datetime))

print()
# Obtain a datetime object representing the epoch: 1st Jan, 1970
epoch = datetime.datetime.utcfromtimestamp(0)
print('epoch                    :', epoch)
print('type(epoch)              :', type(epoch))

print()
# Obtain difference between epoch time and now
delta = now - epoch
print('now - epoch              :', delta)

days = delta.days
print('(now - epoch) diff days  :', days)

seconds = delta.seconds
print('(now - epoch) diff secs  :', seconds)

total_seconds = delta.total_seconds()
print('(now - epoch)total_seconds:', total_seconds)
