def addition(n1, n2):
    return n1 + n2


def multiply(v1, v2):
    return v1 * v2


def hello():
    print('Hello')


if __name__ == '__main__':
    assert addition(10, 20) == 30
    try:
        assert addition(10, 20) == 31, "10 + 20 != 31"
    except AssertionError as ex:
        print(repr(ex))

    assert multiply(10, 20) == 200
    assert multiply(10, 20) != 201

    assert hello() is None
