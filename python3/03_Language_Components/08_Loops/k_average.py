#!/usr/bin/python
"""
Purpose: Calculating the average for the
    inputted numbers in run-time
"""

result = eval("1")
print(f"{result =} {type(result)}")  # int

result = eval("123.23")
print(f"{result =} {type(result)}")  # float

result = eval("12 + 23/32 * 23")
print(f"{result =} {type(result)}")  # float

# result = eval('Apple')
# NameError: name 'Apple' is not defined

result = eval('"Apple"')
print(f"{result =} {type(result)}")  # str

Apple = 12132
result = eval("Apple")
print(f"{result =} {type(result)}")  # int


# Method 1 - Specific no. of times
# summation = 0
# attempt = 0
# while attempt < 5:
#     attempt += 1

#     input_val = eval(input('Enter a number:'))
#     # print(f'{input_val =}')
#     summation += input_val
# else:
#     print(f'{summation =}')
#     average = summation /5
#     print(f'{average   =}')


# average = (12 + 34 + 45) /3

# # Method 2 - Take the no. of attempts val in runtime
# ATTEMPTS = eval(input('\nEnter the no. of values of pass:'))
# summation = 0
# attempt = 0
# while attempt < ATTEMPTS:
#     attempt += 1

#     input_val = eval(input('Enter a number:'))
#     # print(f'{input_val =}')
#     summation += input_val
# else:
#     print(f'{summation =}')
#     average = summation / ATTEMPTS
#     print(f'{average   =}')

# Method 3 - Entering values till the customer need
summation = 0
attempt = 0
while True:
    attempt += 1

    try:
        input_val = eval(input("Enter a number:"))
    except:
        break
    summation += input_val


print(f"{summation =}")
average = summation / attempt
print(f"{average   =}")
