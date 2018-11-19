# Python program to display calendar of given month of the year

# import module
import calendar

yy = 2018
mm = 8

# To ask month and year from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))
print(calendar.month(1945, 8))
print calendar.isleap(2018)

# current year calendar 
print(calendar.calendar(2018, 2, 1, 10))
# print help(calendar)
# print dir(calendar)

