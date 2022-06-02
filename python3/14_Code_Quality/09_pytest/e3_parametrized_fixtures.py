import pytest


@pytest.fixture(name="number", params=(1, 2))
def _number(request):
    """Every time a test requires number, it gets called twice,
    once with 1 and once with 2 passed for number."""
    return request.param


def test_parametrized_fixture(number):
    assert number in {1, 2}
