from customer import Customer

def test_customer_has_default_properties(customer):
    print(f'{id(customer)=}')
    assert customer.cust_id == 100
    assert customer.level == 0

def test_customer_has_initial_level():
    customer = Customer(100, 1)
    print(f'{id(customer)=}')
    assert customer.cust_id == 100
    assert customer.level == 1

def test_customer_level_up_increases_level(customer):
    print(f'{id(customer)=}')
    customer.level_up()
    assert customer.level == 1

def test_customer_level_down_decreases_level(customer):
    print(f'{id(customer)=}')
    customer.level_up()
    customer.level_down()
    assert customer.level == 0

def test_customer_level_not_goes_below_0(customer):
    print(f'{id(customer)=}')
    customer.level_down()
    assert customer.level == 0


# pytest test_customer4.py -rP
# -rP will show output of print statements