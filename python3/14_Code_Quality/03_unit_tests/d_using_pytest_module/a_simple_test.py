#!/usr/bin/python3
"""
Purpose: Simple function with pytest
    a_simple_test.py
    pytest will run all files of the form
    test_*.py or *_test.py in the current directory and its subdirectories.
"""


def func(x):
    return x + 1


def test_func():
    assert func(3) == 4 # 5
