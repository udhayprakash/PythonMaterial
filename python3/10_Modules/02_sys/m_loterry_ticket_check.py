#!/usr/bin/python
"""
Purpose: Lottery Ticket Verifier
"""
import sys

winning_ticket = "123123kj12319088ad"

# Method 1 - using try-exceptions
# try:
#     user_ticket = sys.argv[1]
# except IndexError:
#     print(f'{sys.argv =}')
#     print('Please try your lotter ticket number also')
#     print(f'm_loterry_ticket_check.py <YOUR LOTTERY TICKET NO>')
#     print(f'm_loterry_ticket_check.py 123asdd123rdsr123dsa')
# else:
#     if user_ticket == winning_ticket:
#         print('YOU Won the Lottery!!')
#     else:
#         print('Try Again!!!')

# Method 2
if len(sys.argv) != 2:
    print(f"{sys.argv =}")
    print("Please try your lotter ticket number also")
    print(f"{__file__} <YOUR LOTTERY TICKET NO>")
    print(f"{__file__} 123asdd123rdsr123dsa")
    sys.exit(1)

user_ticket = sys.argv[1]
if user_ticket == winning_ticket:
    print("YOU Won the Lottery!!")
else:
    print("Try Again!!!")
