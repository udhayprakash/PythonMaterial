#!/usr/bin/python
"""
Purpose: Calculator application
	To create documention for this script, use
		python -m pydoc -w calculator
"""

def addition(n1, n2):
    """
    This function will add the two given args, 
    and results it
    :param num1:
    :param num2:
    :return:
    """
    return n1 + n2

def subtraction(n1, n2):
    """
    This function does subtraction operation between the given
    values
    """
    return n1 - n2 

def multipliation(m1, m2):
    return m1 * m2

def division(d1, d2):
    return d1 /d2

if __name__ == '__main__':
    print('This script is executed directly')
    # print(f'addition(100, 200):{addition(100, 200)}')
    print(f'{addition(100, 200)     =}')
    print(f'{subtraction(100, 200)  =}')
    print(f'{multipliation(100, 200)=}')
    print(f'{division(100, 200)     =}')
else:
    print('This script is executed indirectly')
    print(f'{__name__ =}')