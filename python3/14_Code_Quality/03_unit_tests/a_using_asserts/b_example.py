#!/usr/bin/python
"""
Purpose: unit testing using asserts

TDD - Test Driven Development
"""


def addition(n1: int | str | float, n2: int | str | float) -> float:
    return float(n1) + float(n2)


if __name__ == "__main__":
    result = addition(10, 20)
    print(f"{result =}")

    print(f"{result == 30 =}")  # True
    assert result == 30, "Incorrect result"

    assert addition(10, 20) == 30, "Incorrect result"

    assert addition(10, 20.0) == 30.0, "Incorrect result"
    assert addition(10.0, 20) == 30.0, "Incorrect result"
    assert addition(10.0, 20.0) == 30.0, "Incorrect result"

    assert addition(10.0, "20") == 30.0, "Incorrect result"
    assert addition("10", "20") == 30.0, "Incorrect result"

    assert addition("10.0", 20) == 30.0, "Incorrect result"
    assert addition("10.0", "20.0") == 30.0, "Incorrect result"

    try:
        assert addition("10.0", True) == 30.0, "Incorrect result"
    except AssertionError as ex:
        print(repr(ex))
        print(f"{ addition('10.0', True) =}")
