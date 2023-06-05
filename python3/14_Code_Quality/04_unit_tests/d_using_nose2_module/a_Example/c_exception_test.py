def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y


def test_divide_exception():
    assert divide(10, 5) == 2
    try:
        divide(10, 0)
    except ZeroDivisionError as e:
        assert str(e) == "Cannot divide by zero"
