#!/usr/bin/python3
"""
Purpose: Testing exceptions in pytest

"""
import pytest


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0  # 10
        # Fails if ZeroDivisionError is not resulted


# ------Checking for regex matching in exception message


def myfunc():
    raise ValueError('Exception 123 raised')


def test_match():
    with pytest.raises(ValueError, match=r'.* 123 .*'):
        myfunc()

# ----


# @pytest.mark.xfail(raises=IndexError)
# def test_f():
#     f()

def test_exception_message():
    with pytest.raises(ValueError, match='must be 0 or None'):
        raise ValueError('value must be 0 or None')


def test_exception_message_regex():
    with pytest.raises(ValueError, match=r'must be \d+$'):
        raise ValueError('value must be 42')


def test_exception_context():
    with pytest.raises(ValueError) as exc_info:
        raise ValueError('value must be 42')

    assert exc_info.type is ValueError
    assert exc_info.value.args[0] == 'value must be 42'


def test_exception_context_value():
    value = 15
    with pytest.raises(ValueError) as exc_info:
        if value > 10:
            print('value:', value)   # value: 15
            raise ValueError('value must be <= 10')
        assert exc_info.type is ValueError  # this will not execute
    # assert 0  # for demo
