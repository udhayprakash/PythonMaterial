import pytest


@pytest.fixture(params=[1, 2, 3, 4, 5])
def list_of_num(request):
    return request.param


def test_fixture_params(list_of_num):
    print(list_of_num)
