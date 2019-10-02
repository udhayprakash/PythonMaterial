import calendar

# European calendar starts with Monday
c = calendar.TextCalendar()
c.prmonth(2019, 4)

# American calendar starts with Sunday
c = calendar.TextCalendar(calendar.SUNDAY)
c.prmonth(2019, 4)

# Arabic calendar starts with Friday
c = calendar.TextCalendar(calendar.FRIDAY)
c.prmonth(2019, 4)

# In Local language
# https://docs.microsoft.com/en-us/cpp/c-runtime-library/language-strings?view=vs-2017
import locale

for x in locale.windows_locale.values():
    print(x.replace('_', '-'))

c = calendar.LocaleTextCalendar(locale='en-US')
c.prmonth(2019, 4)

# In Local language
c = calendar.LocaleTextCalendar(locale='ru-RU')
c.prmonth(2019, 4)

c = calendar.LocaleTextCalendar(locale='vi-VN')
c.prmonth(2019, 4)

c = calendar.LocaleTextCalendar(locale='sah-RU')
c.prmonth(2019, 4)
