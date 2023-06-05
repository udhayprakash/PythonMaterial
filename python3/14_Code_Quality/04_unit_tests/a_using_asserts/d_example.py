#!/usr/bin/python
"""
Purpose: unit testing using asserts

TDD - Test Driven Development
"""


def hello_world(name: str = "World!") -> str:
    return f"Hello {name}"


if __name__ == "__main__":
    # calling the function
    print(hello_world("Python"))

    # adding the assertions
    assert hello_world("Python") == "Hello Python"
    try:
        assert hello_world() == "Hello World"
    except AssertionError as ex:
        print(ex)
        print(hello_world())

    assert hello_world() == "Hello World!"
