from unittest import TestCase, main 
from unittest.mock import patch


foo = 'Hello'
bar = 'Goodbye'

# NOTE: 'new' will mock one existing object 
# with another. Here, objects are not callable
class MyTest(TestCase):
    @patch('__main__.foo', new=bar)
    def test_foo(self):
        print(foo)     # Goodbye


if __name__ == "__main__":
    main()