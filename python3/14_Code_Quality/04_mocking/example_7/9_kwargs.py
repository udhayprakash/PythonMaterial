from unittest.mock import patch

# kwargs
# @patch('my_module.Foo.name', return_value='Python')

# @patch('my_module.Foo', name='Python', version=3.8)

# @patch('my_module.Foo', **{'name.return_value': 'Python'})


# patch.object
# patch.dict
# patch.multiple


# patch.dict() for setting values in a dictionary just during
# a scope and restoring the dictionary to its original state
# when the test ends:
foo = {'key': 'value'}
original = foo.copy()

with patch.dict(foo, {'newkey': 'newvalue'}, clear=True):
    assert foo == {'newkey': 'newvalue'}

assert foo == original
