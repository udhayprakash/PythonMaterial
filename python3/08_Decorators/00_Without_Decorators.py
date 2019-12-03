#!/usr/bin/python
"""
Without decorators
"""


# def add(a, b):
#     return a + b


# def div(n1, n2):
#     return n1 / n2

# ------------------------------
def add(a, b):
    try:
        result = a + b
    except Exception as ex:
        return ex
    else:
        return result


def div(n1, n2):
    try:
        result = n1 / n2
    except Exception as ex:
        return ex
    else:
        return result


if __name__ == '__main__':
    print(add(12, 34))
    print(add('12', '34'))
    print(add(12, '34'))
    print(add('12', 34))

    print(div(10, 5))
    print(div(0, 5))
    print(div(5, 0))
