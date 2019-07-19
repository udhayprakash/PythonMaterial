# Python program to check if the input year is a leap year or not

# year = 2018

# To get year (integer input) from the user
year = int(input('year=')

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    else:
        print("{0} is not a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))

##################################################
if (year % 4) == 0) and (year % 100) == 0) and (year % 400) == 0):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))

##################################################
if (not year % 4) and (not year % 100) and (not year % 400):
    # 0               0                  0
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))

##################################################
if not( year % 4 or  year % 100 or  year % 400):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))