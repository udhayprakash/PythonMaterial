#!/usr/bin/python
# http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/

def outer(func):
    def inner(v1, v2):
        try:
            result = func(v1, v2)  # add(a, b)
        except Exception as ex:
            return ex
        else:
            return result

    return inner


def add(a, b):
    return a + b


def div(n1, n2):
    return n1 / n2


if __name__ == '__main__':
    temp_var = outer(add)  # reference  to inner
    # print(temp_var)
    print('temp_var(2, 3)  ', temp_var(2, 3))
    assert add(2, 3) == temp_var(2, 3) == outer(add)(2, 3)

    temp_var = outer(div)  # reference  to inner
    print('temp_var(2, 3)  ', temp_var(2, 3))
    assert div(2, 3) == temp_var(2, 3) == outer(div)(2, 3)
