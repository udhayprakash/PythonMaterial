import calendar

given_input = '08 23 2019' # "MM DD YYYY" # input()
month, day, year = map(int, given_input.split(' '))

weeks = ('MONDAY','TUESDAY','WEDNESDAY','THURSDAY',
            'FRIDAY','SATURDAY','SUNDAY')
print(calendar.weekday(year, month, day))

print(weeks[calendar.weekday(year, month, day)])
