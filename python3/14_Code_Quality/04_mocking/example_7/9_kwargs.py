kwargs
@patch('my_module.Foo.name', return_value='Python')

@patch('my_module.Foo', name='Python', version=3.8)

@patch('my_module.Foo', **{'name.return_value': 'Python'})


patch.object 
patch.dict 
patch.multiple

