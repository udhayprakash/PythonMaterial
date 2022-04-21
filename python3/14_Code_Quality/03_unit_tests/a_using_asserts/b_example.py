#!/usr/bin/python
"""
Purpose: unit testing using asserts

TDD - Test Driven Development
"""

def addition(n1, n2):
    return float(n1) + float(n2)
    # return int(n1) + int(n2)
    # return n1 + n2


if __name__ == '__main__':
    result = addition(10, 20)
    print(f'{result =}')

    print(f'{result == 30 =}')

    assert addition(10, 20) == 30, 'Incorrect result'

    assert addition(10, 20.0) == 30.0, 'Incorrect result'
    assert addition(10.0, 20) == 30.0, 'Incorrect result'
    assert addition(10.0, 20.0) == 30.0, 'Incorrect result'

    assert addition(10.0, '20') == 30.0, 'Incorrect result'
    assert addition('10', '20') == 30.0, 'Incorrect result'

    assert addition('10.0', 20) == 30.0, 'Incorrect result'
    assert addition('10.0', '20.0') == 30.0, 'Incorrect result'

    try:
        assert addition('10.0', True) == 30.0, 'Incorrect result'
    except AssertionError as ex:
        print(repr(ex))
        print(f"{ addition('10.0', True) =}")
