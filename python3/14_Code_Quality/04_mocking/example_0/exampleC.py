from unittest import TestCase, main
from unittest.mock import Mock


def foo(some_object, number):
    if number > 2:
        some_object.method(number**2)
    else:
        some_object.method(number - 1)


class FooTests(TestCase):
    def test_foo_for_2_calls_method_with_1(self):
        some_object = Mock(method=Mock())

        foo(some_object, 2)

        some_object.method.assert_called_once_with(1)


if __name__ == "__main__":
    main()
