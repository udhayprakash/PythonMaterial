# -*- coding: utf-8 -*-
"""
Python script to check validity of credit card numbers

Generating check digit:

Lets assume you have a number given below:
3 – 7 – 5 – 6 – 2 – 1 – 9 – 8 – 6 – 7 – X
X is the check digit.
Now starting from the right most digit i.e. check digit, double the every second digit.
New number will be:
3 – 14 – 5 – 12 – 2 – 2 – 9 – 16 – 6 – 14 – X
Now if double of a digit is more then 9, add the digits.
So the number will become:
3 – 5 – 5 – 3 – 2 – 2 – 9 – 7 – 6 – 5 – X
Now add all digits.
47 + X
Multiply the non-check part by 9.
47 * 9 = 423
Unit digit in the multiplication result is the check digit. X = 3
Valid number would be 37562198673.
"""
import sys


def usage():
    msg = """
        
        usage:
        python3 credit_card_validator credit_card_number
        
        example:
        python3 credit_card_validator 34678253793
        
    """
    print(msg)


def get_cc_number():
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    return sys.argv[1]


def sum_digits(digit):
    if digit < 10:
        return digit
    else:
        sum = (digit % 10) + (digit // 10)
        return sum


def validate(cc_num):
    # reverse the credit card number
    cc_num = cc_num[::-1]
    # convert to integer
    cc_num = [int(x) for x in cc_num]
    # double every second digit
    doubled_second_digit_list = list()
    digits = list(enumerate(cc_num, start=1))
    for index, digit in digits:
        if index % 2 == 0:
            doubled_second_digit_list.append(digit * 2)
        else:
            doubled_second_digit_list.append(digit)

    # add the digits if any number is more than 9
    doubled_second_digit_list = [sum_digits(x) for x in doubled_second_digit_list]
    # sum all digits
    sum_of_digits = sum(doubled_second_digit_list)
    if sum_of_digits % 10 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    print(validate(get_cc_number()))
