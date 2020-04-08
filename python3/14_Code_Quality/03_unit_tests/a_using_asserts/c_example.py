#!/usr/bin/python
"""
Purpose:
"""


def hello_world(name='World'):
    return f'Hello {name}'


if __name__ == '__main__':
    # function call
    print(hello_world('Python'))

    # Adding the assertions
    assert hello_world() == 'Hello World'
    assert hello_world() == 'Hello world'
