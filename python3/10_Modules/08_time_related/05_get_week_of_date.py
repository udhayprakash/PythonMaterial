import calendar

given_input = '08 05 2015' # "MM DD YYYY" # input()
month, day, year = map(int, given_input.split(' '))

week_dict = ('MONDAY','TUESDAY','WEDNESDAY','THURSDAY',
            'FRIDAY','SATURDAY','SUNDAY')
print(week_dict[calendar.weekday(year, month, day)])
