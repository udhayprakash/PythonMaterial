import datetime as dtm

local_now = dtm.datetime.now()
print('local now: {}'.format(local_now))

utc_now = dtm.datetime.utcnow()
print('utc now  : {}'.format(utc_now))

print()
# You can access any value separately:
print('{} {} {} {} {} {}'.format(local_now.year, local_now.month,
                                 local_now.day, local_now.hour,
                                 local_now.minute, local_now.second))

print('date: {}'.format(local_now.date()))
print('time: {}'.format(local_now.time()))

print()
# datetime.strftime - For string formatting the datetime
# For more datetime related string formatters, go to http://strftime.org/
print('%Y/%m/%d-%H:%M:%S', local_now.strftime('%Y/%m/%d-%H:%M:%S'))
print('%y/%m/%d-%H:%M:%S', local_now.strftime('%y/%m/%d-%H:%M:%S'))
print('%y %m %d-%H:%M:%S', local_now.strftime('%y %m %d-%H:%M:%S'))
print('%y %m %d-%I:%M:%S %p', local_now.strftime('%y %m %d-%I:%M:%S %p'))

formatted2 = local_now.strftime('date: %d %b,%Y time:%H:%M:%S')
print('formatted2', formatted2)


# datetime.strptime() - For converting a datetime string into a datetime object
my_dt = dtm.datetime.strptime('2000-01-01 10:00:00', '%Y-%m-%d %H:%M:%S')
print(f'my_dt:{my_dt} type(my_dt):{type(my_dt)}')


# datetime.timedelta - For working with time difference.
tomorrow = local_now + dtm.timedelta(days=1)
print('tomorrow this time: {}'.format(tomorrow))

delta = tomorrow - local_now
print('tomorrow - now = {}'.format(delta))
print('days: {}, seconds: {}'.format(delta.days, delta.seconds))
print('total seconds: {}'.format(delta.total_seconds()))
