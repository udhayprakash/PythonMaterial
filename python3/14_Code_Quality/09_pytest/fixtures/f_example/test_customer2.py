import pytest
from customer import Customer


@pytest.fixture
def customer():
    _customer = Customer(100)
    return _customer


def test_customer_has_default_properties(customer):
    """Using fixture"""
    assert customer.cust_id == 100
    assert customer.level == 0


def test_customer_has_initial_level():
    """WITHOUT using fixtures"""
    customer = Customer(100, 1)
    assert customer.cust_id == 100
    assert customer.level == 1


def test_customer_level_up_increases_level(customer):
    customer.level_up()
    assert customer.level == 1


def test_customer_level_down_decreases_level(customer):
    customer.level_up()
    customer.level_down()
    assert customer.level == 0


def test_customer_level_not_goes_below_0(customer):
    customer.level_down()
    assert customer.level == 0
