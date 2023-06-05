"""
Purpose: unit testing using asserts

TDD - Test Driven Development
"""
from typing import Any


def hello(name: Any) -> None:
    print(name)


if __name__ == "__main__":
    # calling the function
    hello("Udhay")

    # Adding the assertions
    assert hello("Udhay") == None
    assert hello("Udhay") is None
    assert hello("Python") is None
    assert hello("Gudo") is None
