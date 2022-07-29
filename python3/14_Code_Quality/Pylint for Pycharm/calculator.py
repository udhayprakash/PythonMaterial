#!/usr/bin/python

"""
Purpose: Simple Calculator Application
"""
__author__ = ""


def addition(a, b):
    """
    Performs addition operation between 'a' and 'b'
    :param a:  Integer
    :param b:  Integer
    :return:   Integer
    """
    return a + b


def subtraction(a, b):
    """
    Performs subtraction operation between 'a' and 'b'
    :param a:  Integer
    :param b:  Integer
    :return:   Integer
    """
    return a - b


def multiplication(a, b):
    """
    Performs multiplication operation between 'a' and 'b'
    :param a:  Integer
    :param b:  Integer
    :return:   Integer
    """
    return a * b


def division(a, b):
    """
    :param a:  Integer
    :param b:  Integer
    :return:   Integer
    """
    return a / float(b)


if __name__ == "__main__":
    print("addition(a,b) = ", addition(5, 3))
    print("subtraction(a,b) = ", subtraction(5, 3))
    print("multiplication(a,b) = ", multiplication(5, 3))
