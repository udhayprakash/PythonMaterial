#!/usr/bin/python
"""
Purpose:
"""
from typing import Any


def hello(name: Any) -> None:
    print(name)


if __name__ == '__main__':
    # calling the function
    hello('Python')

    # Adding the assertions
    # assert hello('Python') == None
    assert hello('Python') is None
    assert hello('Udhay') is None
    assert hello('prakash') is None
