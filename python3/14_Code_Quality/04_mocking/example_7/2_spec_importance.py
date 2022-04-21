from unittest.mock import patch, Mock
from unittest import TestCase, main
# speccing solves mocking problem

def foo(arg):
    pass

def bar():
    return foo('Bob')

class MyTest(TestCase):
    @patch('__main__.foo')
    def test_bar(self, mock_foo):
        bar()
        mock_foo.assrt_called_with('Bob')  # PASS

class MyTest2(TestCase):
    @patch('__main__.foo', spec=True)
    def test_bar(self, mock_foo):
        bar()
        mock_foo.assrt_called_with('Bob')  # Exception

if __name__ == '__main__':
    main()
