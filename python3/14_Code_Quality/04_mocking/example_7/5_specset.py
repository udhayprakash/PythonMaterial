from unittest import TestCase, main
from unittest.mock import Mock, patch


class Foo:
    def __init__(self):
        x = 20

    def bar(self):
        pass


class TestFoo(TestCase):
    @patch("__main__.Foo", autospec=True, spec_set=True)
    def test_bar(self, mock_foo):
        f = mock_foo()
        f.x = 20  # AttributeError: Mock object has no attribute 'x'


# NOTE: spec_set prevents from setting attributes
# which dont exist

if __name__ == "__main__":
    main()
