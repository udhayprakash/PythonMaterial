import pytest


def test_passes():
    with pytest.raises(Exception) as e_info:
        x = 1 / 0


def test_passes_without_info():
    with pytest.raises(Exception):
        x = 1 / 0


def test_fails():
    with pytest.raises(Exception) as e_info:
        x = 1 / 1


def test_fails_without_info():
    with pytest.raises(Exception):
        x = 1 / 1

# Don't do this. Assertions are caught as exceptions.


def test_passes_but_should_not():
    try:
        x = 1 / 1
        assert False
    except Exception:
        assert True

# Even if the appropriate exception is caught, it is bad style,
# because the test result is less informative
# than it would be with pytest.raises(e)
# (it just says pass or fail.)


def test_passes_but_bad_style():
    try:
        x = 1 / 0
        assert False
    except ZeroDivisionError:
        assert True


def test_fails_but_bad_style():
    try:
        x = 1 / 1
        assert False
    except ZeroDivisionError:
        assert True


if __name__ == '__main__':
    test_passes()
    test_passes_without_info()
    test_fails()
    test_fails_without_info()
    test_passes_but_should_not()
    test_passes_but_bad_style()
    test_fails_but_bad_style()



# python -m py.test