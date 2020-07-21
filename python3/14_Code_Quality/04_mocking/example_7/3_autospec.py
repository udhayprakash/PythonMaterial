from unittest.mock import patch, Mock
from unittest import TestCase, main

class Foo:
    def bar(self):
        pass 

class TestFoo(TestCase):
    @patch('__main__.Foo', spec=True)
    def test_bar(self, mock_foo):
        f = mock_foo()
        f.bar()
        mock_foo.bar.assrt_called_with() # PASS

# NOTE: spec cant find objects within objects. 
# so, we should go with autospec
class TestFoo2(TestCase):
    @patch('__main__.Foo', autospec=True)
    def test_bar(self, mock_foo):
        f = mock_foo()
        f.bar()
        mock_foo.bar.assrt_called_with() # AttributeError



if __name__ == '__main__':
    main()