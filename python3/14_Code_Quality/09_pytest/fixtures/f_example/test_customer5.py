from customer import Customer

def test_customer_session_has_default_properties(customer_session):
    print(f'{id(customer_session)=}')
    assert customer_session.cust_id == 100
    assert customer_session.level == 0

def test_customer_session_has_initial_level():
    customer_session = Customer(100, 1)
    print(f'{id(customer_session)=}')
    assert customer_session.cust_id == 100
    assert customer_session.level == 1

def test_customer_session_level_up_increases_level(customer_session):
    print(f'{id(customer_session)=}')
    original_level = customer_session.level
    customer_session.level_up()
    assert customer_session.level == original_level + 1

def test_customer_session_level_down_decreases_level(customer_session):
    print(f'{id(customer_session)=}')
    original_level = customer_session.level
    customer_session.level_up()
    customer_session.level_down()
    assert customer_session.level == original_level

def test_customer_session_level_not_goes_below_0(customer_session):
    print(f'{id(customer_session)=}')
    original_level = customer_session.level
    customer_session.level_down()
    assert customer_session.level == (original_level - 1 if original_level >= 1 else 0)
