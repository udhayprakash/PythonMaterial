#!/usr/bin/python3
"""
Purpose: Simple function with pytest
    b_sysexit_test.py

    Running pytest on this script
        ~pytest b_sysexit_test.py

    Running quitely
        ~pytest --quiet b_sysexit_test.py
        ~pytest -q b_sysexit_test.py

"""
import pytest


def func():
    raise SystemExit(1)


def test_func():
    with pytest.raises(SystemExit):
        func()


def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:

        def f():
            f()

        f()
    assert "maximum recursion" in str(excinfo.value)
