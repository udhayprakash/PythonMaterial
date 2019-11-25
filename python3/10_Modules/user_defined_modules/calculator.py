#!/usr/bin/python
"""
Purpose: Calculator application
	To create documention for this script, use
		python -m pydoc -w calculator
"""

PI = 3.141516

def addition(num1, num2):
    """
    This function will add the two given args, and results it
    :param num1:
    :param num2:
    :return:
    """
    return num1 + num2


def subtraction(num1, num2):
    """
    This function does subtraction operation between the given
    values
    """
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


if __name__ == '__main__':
    print('The script was executed directly')
    print(f'addition(12, 10)        :{addition(12, 10)}')
    print(f'subtraction(12, 10)     :{subtraction(12, 10)}')
    print(f'multiplication(12, 10)  :{multiplication(12, 10)}')
    print(f'division(12, 10)        :{division(12, 10)}')
else:
    print('The script was imported in another script/terminal')
