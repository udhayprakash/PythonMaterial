#!/usr/bin/python3
"""
Purpose: Office Schedule
    Monday to Friday  :- 9 am to 6 pm
    Saturday          :- 9 am to 1 pm
    Sunday            :- Holiday

"""

# week_of_day = 'Monday'
week_of_day = input("Enter week of the day:").title().strip()

# Method 4
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


# Method 5

match week_of_day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("TIMINGS: 9 AM to 6 PM")
    case "Saturday":
        print("TIMINGS: 9 AM to 1 PM")
    case "Sunday":
        print("----HOLIDAY----------")
    case _:
        print("INVALID ENTRY! PLEASE TRY AGAIN!!")
