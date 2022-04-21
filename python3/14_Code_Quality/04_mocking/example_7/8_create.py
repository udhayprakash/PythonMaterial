from unittest import TestCase, main
from unittest.mock import patch


class Foo:
    def bar(self):
        pass


# NOTE: create will come by default in new versions of python
# In older version of python < 3.4, it is needed
# to be able to create attributes to this mock object
class TestFoo(TestCase):
    @patch("__main__.Foo.bar", create=True)
    def test_foo(self, mock_bar):
        pass


if __name__ == "__main__":
    main()
