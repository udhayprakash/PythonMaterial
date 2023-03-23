#!/usr/bin/python
"""
Purpose: datetime.date
"""

from datetime import date, datetime, timedelta

today = date.today()
print(today)  # 2020-06-24
print("ctime  :", today.ctime())  # Wed Jun 24 00:00:00 2020
print("tuple  :", today.timetuple())
# time.struct_time(tm_year=2020, tm_mon=6, tm_mday=24, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=2, tm_yday=176, tm_isdst=-1)

print("Ordinal:", today.toordinal())  # 737600

print()
print("year  :", today.year)  # 2020
print("Month :", today.month)  # 6
print("Day   :", today.day)  # 24
print()


def next_consec_friday(given_date: str) -> None:
    """given a date, get next consecutive friday
    M T W Th F
    0 1 2 3  4
    """
    date_obj = datetime.strptime(given_date, "%d-%m-%Y")
    days_till_friday = (4 - date_obj.weekday()) % 7
    friday_date = date_obj + timedelta(days=days_till_friday)
    return friday_date.strftime("%d-%m-%Y")


print(next_consec_friday("20-03-2023"))  # 24-03-2023
print(next_consec_friday("24-03-2023"))  # 24-03-2023
print(next_consec_friday("25-03-2023"))  # 31-03-2023
print(next_consec_friday("29-03-2023"))  # 31-03-2023
