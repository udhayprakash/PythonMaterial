import pytest
import time 
from datetime import datetime

@pytest.fixture(autouse=True)
def time_calculator():
    print(f" Test started: {datetime.now().strftime('%d-%m-%Y %H:%M')} ")
    yield
    print(f" Test ended: {datetime.now().strftime('%d-%m-%Y %H:%M')} ")

def test_fixture_scope():
    time.sleep(2)
