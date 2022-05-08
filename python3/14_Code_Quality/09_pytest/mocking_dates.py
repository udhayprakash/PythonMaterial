import datetime
from unittest.mock import patch

import pytest


def get_utcnow_isoformat() -> str:
    """Get UTCnow as an isoformat compliant string."""
    return datetime.datetime.utcnow().isoformat()


@pytest.fixture
def mock_datetime():
    with patch("datetime.datetime") as m:
        # This is where the magic happens!
        m.utcnow.return_value.isoformat.return_value = "2022-03-15T23:11:12.432048"
        yield m


def test_get_utcnow_isoformat(mock_datetime):
    frozen_date = "2022-03-15T23:11:12.432048"
    assert get_utcnow_isoformat() == frozen_date


# python -m pytest mocking_dates.py
