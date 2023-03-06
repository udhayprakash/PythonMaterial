import string


def add(a, b):
    """Simple function to add two numbers"""
    return a + b


def test_add():
    assert add(2, 4) == 6, "The correct answer should be 6"


# -------------------------------------


def test_square():
    n = 2
    assert n * n == 4


def test_cube():
    n = 2
    assert n * n * n == 8


def test_case01():
    assert "python".upper() == "PYTHON"


def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"


def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]


def test_some_primes():
    assert 37 in {
        num
        for num in range(1, 50)
        if num != 1 and not any([num % div == 0 for div in range(2, num)])
    }


# -------------------------------------


class TestClass01:
    def test_case01(self):
        assert "python".upper() == "PYTHON"

    def test_case02(self):
        assert "PYTHON".lower() == "python"


# -------------------------------------


def is_valid_email_address(s):
    s = s.lower()
    parts = s.split("@")
    if len(parts) != 2:
        # Not exactly one at-sign
        return False
    allowed = set(string.ascii_lowercase + string.digits + ".-_")
    for part in parts:
        if not set(part) <= allowed:
            # Characters other than the allowed ones are found
            return False
    return True


print(is_valid_email_address("test@example.org"))  # True
print(is_valid_email_address("user123@subdomain.example.org"))  # True
print(is_valid_email_address("john.doe@email.example.org"))  # True
print(is_valid_email_address("not valid@example.org"))  # False
print(is_valid_email_address("john.doe"))  # False
print(is_valid_email_address("john,doe@example.org"))


def test_regular_email_validates():
    assert is_valid_email_address("test@example.org")
    assert is_valid_email_address("user123@subdomain.example.org")
    assert is_valid_email_address("john.doe@email.example.org")


def test_valid_email_has_one_at_sign():
    assert not is_valid_email_address("john.doe")


def test_valid_email_has_only_allowed_chars():
    assert not is_valid_email_address("john,doe@example.org")
    assert not is_valid_email_address("not valid@example.org")


# py -m pytest 0_example.py
