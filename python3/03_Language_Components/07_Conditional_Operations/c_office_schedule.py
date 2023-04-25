#!/usr/bin/python3
"""
Purpose: Office Schedule
    Monday to Friday  :- 9 am to 6 pm
    Saturday          :- 9 am to 1 pm
    Sunday            :- Holiday

    In runtime, user will give week name, and they should be that day schedule
"""
# week_of_day = "Monday"
week_of_day = input("Enter week of the day:").strip().title()


# # Method 1
# if week_of_day == "Monday":
#     print("TIMINGS: 9 AM to 6 PM")
# elif week_of_day == "Tuesday":
#     print("TIMINGS: 9 AM to 6 PM")
# elif week_of_day == "Wednesday":
#     print("TIMINGS: 9 AM to 6 PM")
# elif week_of_day == "Thursday":
#     print("TIMINGS: 9 AM to 6 PM")
# elif week_of_day == "Friday":
#     print("TIMINGS: 9 AM to 6 PM")
# elif week_of_day == "Saturday":
#     print("TIMINGS: 9 AM to 1 PM")
# elif week_of_day == "Sunday": # or week_of_day == "sunday" or  or week_of_day == "SUNday":
#     print("----HOLIDAY----------")
# else:
#     print("INVALID ENTRY! PLEASE TRY AGAIN!!")


# # Method 2
# WEEKDAY_TIMINGS = "TIMINGS: 9 AM to 6 PM"
# if week_of_day == "Monday":
#     print(WEEKDAY_TIMINGS)
# elif week_of_day == "Tuesday":
#     print(WEEKDAY_TIMINGS)
# elif week_of_day == "Wednesday":
#     print(WEEKDAY_TIMINGS)
# elif week_of_day == "Thursday":
#     print(WEEKDAY_TIMINGS)
# elif week_of_day == "Friday":
#     print(WEEKDAY_TIMINGS)
# elif week_of_day == "Saturday":
#     print("TIMINGS: 9 AM to 1 PM")
# elif week_of_day == "Sunday":
#     print("----HOLIDAY----------")
# else:
#     print("INVALID ENTRY! PLEASE TRY AGAIN!!")

# METHOD 3
# WEEKDAY_TIMINGS = "TIMINGS: 9 AM to 6 PM"
# if (week_of_day == "Monday"
#     or week_of_day == "Tuesday"
#     or week_of_day == "Wednesday"
#     or week_of_day == "Thursday"
#     or week_of_day == "Friday"):  # 5 relational ops + 4 logical ops -- Short circuit
#     print(WEEKDAY_TIMINGS)
# elif week_of_day == "Saturday":
#     print("TIMINGS: 9 AM to 1 PM")
# elif week_of_day == "Sunday":
#     print("----HOLIDAY----------")
# else:
#     print("INVALID ENTRY! PLEASE TRY AGAIN!!")


# METHOD 4 - MEMBERSHIP CHECK
# in - membership check operator
# in operator works with any iterable object

if week_of_day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    print("TIMINGS: 9 AM to 6 PM")
elif week_of_day == "Saturday":
    print("TIMINGS: 9 AM to 1 PM")
elif week_of_day == "Sunday":
    print("----HOLIDAY----------")
else:
    print("INVALID ENTRY! PLEASE TRY AGAIN!!")
# NOTE: else is optional
