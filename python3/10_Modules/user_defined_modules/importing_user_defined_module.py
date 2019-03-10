import newScript
print(dir(newScript))

print(newScript.multiplication(9, 18))
print('newScript.__file__           ', newScript.__file__)
print('newScript.__name__           ', newScript.__name__)
print('newScript.__package__        ', newScript.__package__)

print('callable(newScript.vowels)   ', callable(newScript.vowels))
print('callable(newScript.subtraction)', callable(newScript.subtraction))
help(newScript)