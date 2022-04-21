#!/usr/bin/python3
"""
Purpose: Using Custom Exception
"""
# # Method 1 - stop when exception is raised
# try:
#     votes = 0
#     i = 0
#     while i < 5:
#         age = int(input('Enter your age:'))
#         if age <= 0:
#             raise Exception('Invalid Entry for the age!')
#         elif age < 18:
#             raise Exception('You are Ineligible to vote!!')
#         else:
#             votes += 1
#         i += 1
# except Exception as ex:
#     print(f'{ex=}')
#
# print(f"Total Eligible Voters: {votes}")


# Method 2 - skip the loop with exception
class InvalidInput(Exception):
    pass


class InvalidAge(Exception):
    pass


votes = 0
attempt = 0
while attempt < 5:
    print(f"\n{attempt =}")
    try:
        age = int(input("Enter your age:"))
        if age <= 0:
            raise InvalidInput("Invalid Entry for the age!")
        elif age < 18:
            # raise InvalidAge('You are Ineligible to vote!!')
            raise InvalidAge(f"You are short by {18 - age} years for voting")
        else:
            votes += 1
        attempt += 1
    except Exception as ex:
        print(f"{ex=}")
    else:
        print(f"Your voterID is {attempt}")
