from customer import Customer
import pytest

@pytest.fixture
def customer():
    _customer = Customer(100)
    return _customer

@pytest.fixture(scope='session')
def customer_session():
    _customer = Customer(100)
    return _customer



