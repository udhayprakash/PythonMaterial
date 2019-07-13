import calendar

given_input = '08 05 2015' # "MM DD YYYY" # input()
month, day, year = map(int, given_input.split(' '))

weeks = ('MONDAY','TUESDAY','WEDNESDAY','THURSDAY',
            'FRIDAY','SATURDAY','SUNDAY')
print(weeks[calendar.weekday(year, month, day)])
