from unittest.mock import patch

class Foo():
    x = 20
    def bar(self):
        y = 10
        return y 
    
print(dir(Foo))

print()
with patch('__main__.Foo') as mock_foo:
    print(dir(mock_foo))  # no x, y attributes

print()
# spec - will create mock object as the orignal
with patch('__main__.Foo', spec=True) as mock_foo:
    print(dir(mock_foo))  # no x, y attributes


