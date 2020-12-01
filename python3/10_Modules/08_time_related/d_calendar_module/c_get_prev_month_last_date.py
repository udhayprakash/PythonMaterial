import datetime as dt 
import calendar

# today = dt.datetime.now().year
# calendar.monthrange(today.year)

# base = dt.datetime.today()
# numdays = 5
# date_list = [base - dt.timedelta(days=x) for x in range(numdays)]
# print(date_list)

import datetime as dt
today = dt.datetime.now()
prev_month_last_day = today - dt.timedelta(days=today.day)

print(f'{today.year  =}')
print(f'{today.month =}')
print(f'{today.day   =}')
print(dir(today))

last_day = calendar.monthrange(today.year, today.month)[1]


