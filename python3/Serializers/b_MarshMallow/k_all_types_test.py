import pytest
from k_all_types import ExampleEnum, MyExampleSchema
from marshmallow import ValidationError


def test_my_example_schema():
    schema = MyExampleSchema()

    # Test all fields with valid values
    valid_data = {
        "my_field": "field value",
        "my_raw": {"key": "value"},
        "my_nested": {"my_field": "nested value"},
        "my_mapping": {"key1": 1, "key2": 2},
        "my_dict": {"key1": "value1", "key2": "value2"},
        "my_list": ["value1", "value2"],
        "my_tuple": (1, 2),
        "my_string": "string value",
        "my_uuid": "d0c64f64-0f74-4bb4-9e3d-3b05ac9fa4ad",
        "my_number": 1.23,
        "my_integer": 123,
        "my_decimal": "1.23",
        "my_boolean": True,
        "my_float": 1.23,
        "my_datetime": "2022-03-31T12:34:56.789000+00:00",
        "my_naive_datetime": "2022-03-31T12:34:56.789000",
        "my_aware_datetime": "2022-03-31T12:34:56.789000+00:00",
        "my_time": "12:34:56.789000",
        "my_date": "2022-03-31",
        "my_timedelta": "1 day, 1:23:45.678900",
        "my_url": "http://example.com",
        "my_URL": "http://example.com",
        "my_email": "user@example.com",
        "my_ip": "192.0.2.1",
        "my_ipv4": "192.0.2.1",
        "my_ipv6": "2001:db8::1",
        "my_ip_interface": "192.0.2.1/24",
        "my_ipv4_interface": "192.0.2.1/24",
        "my_ipv6_interface": "2001:db8::1/64",
        "my_enum": ExampleEnum.VALUE1,
        "my_method": "field value",
        "my_function": "FIELD VALUE",
        "my_str": "string value",
        "my_bool": True,
        "my_int": 123,
        "my_constant": "some constant value",
        "my_pluck": "some other field value",
    }

    result = schema.load(valid_data)
    assert result == valid_data


def test_my_example_schema_negative():
    # Test invalid values
    invalid_data = {
        "my_field": 123,  # Invalid type
        "my_raw": object(),  # Invalid type
        "my_nested": {"invalid_field": "nested value"},  # Invalid field
        "my_mapping": {"key1": "value1"},  # Invalid value type
        "my_dict": {"key1": 123},  # Invalid value type
        "my_list": "not a list",  # Invalid type
        "my_tuple": (1, 2, 3),  # Invalid length
        "my_string": "too long string value that exceeds the maximum length limit",  # Exceeds max length
        "my_uuid": "not a uuid",
        "my_number": "not a number",  # Invalid type
        "my_integer": 12.3,  # Invalid type
        "my_decimal": 1.23,  # Invalid type
        "my_boolean": "not a boolean",  # Invalid type
        "my_float": "not a float",  # Invalid type
        "my_datetime": "invalid datetime",  # Invalid format
        "my_naive_datetime": "invalid datetime",  # Invalid format
        "my_aware_datetime": "invalid datetime",  # Invalid format
        "my_time": "invalid time",  # Invalid format
        "my_date": "invalid date",  # Invalid format
        "my_timedelta": "invalid timedelta",  # Invalid format
        "my_url": "invalid url",  # Invalid format
        "my_URL": "invalid url",  # Invalid format
        "my_email": "invalid email",  # Invalid format
        "my_ip": "invalid ip",  # Invalid format
        "my_ipv4": "invalid ipv4",  # Invalid format
        "my_ipv6": "invalid ipv6",  # Invalid format
        "my_ip_interface": "invalid ip interface",  # Invalid format
        "my_ipv4_interface": "invalid ipv4 interface",  # Invalid format
        "my_ipv6_interface": "invalid ipv6 interface",  # Invalid format
        "my_enum": "invalid enum value",  # Invalid value
        "my_method": 123,  # Invalid type
        "my_function": 123,  # Invalid type
        "my_str": 123,  # Invalid type
        "my_bool": "not a boolean",  # Invalid type
        "my_int": "not an integer",  # Invalid type
        "my_constant": 123,  # Invalid type
        "my_pluck": {"key": "value"},  # Invalid type
    }
