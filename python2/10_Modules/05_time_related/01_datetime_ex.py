from __future__ import print_function
import datetime as dt

local_now = dt.datetime.now()
print('local now: {}'.format(local_now))

utc_now = dt.datetime.utcnow()
print('utc now  : {}'.format(utc_now))

# You can access any value separately:
print('{} {} {} {} {} {}'.format(local_now.year, local_now.month,
                                 local_now.day, local_now.hour,
                                 local_now.minute, local_now.second))

print('date: {}'.format(local_now.date()))
print('time: {}'.format(local_now.time()))

# datetime.strftime - For string formatting the datetime
# For more datetime related string formatters, go to http://strftime.org/
formatted1 = local_now.strftime('%Y/%m/%d-%H:%M:%S')
print(formatted1)

formatted2 = local_now.strftime('date: %d %b,%Y time:%H:%M:%S')
print(formatted2)


# datetime.strptime() - For converting a datetime string into a datetime object
my_dt = dt.datetime.strptime('2000-01-01 10:00:00', '%Y-%m-%d %H:%M:%S')
print('my_dt: {}'.format(my_dt))


# datetime.timedelta - For working with time difference.
tomorrow = local_now + dt.timedelta(days=1)
print('tomorrow this time: {}'.format(tomorrow))

delta = tomorrow - local_now
print('tomorrow - now = {}'.format(delta))
print('days: {}, seconds: {}'.format(delta.days, delta.seconds))
print('total seconds: {}'.format(delta.total_seconds()))
