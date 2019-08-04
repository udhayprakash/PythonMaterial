
# ways of creating dictionary 
a = dict(one=1, two=2, three=3)

b = {'one': 1, 'two': 2, 'three': 3}

c = dict(
    zip(['one', 'two', 'three'], [1, 2, 3])
    )
d = dict([('two', 2), ('one', 1), ('three', 3)])

e = dict({'three': 3, 'one': 1, 'two': 2})
print('all are ', a == b == c == d == e)

# ############
data = [(1, 'red'), (2, 'blue'), (3, 'yellow')]
print(dict(data))

data = [('red', 1), ('blue', 2), ('yellow', 3)]
print(dict(data))

data = (('red', 1), ('blue', 2), ('yellow', 3))
print(dict(data))

data = (['red', 1], ['blue', 2], ('yellow', 3))
print(dict(data))
##################
cities = ('New York', 'Shangai', 'New Delhi')
countries = {'US', 'China'}

# list of tuples
print('\n', list(zip(cities, countries)))

cities_n_countries = dict(zip(countries, cities))

print('\ncities_n_countries\n', cities_n_countries)
print(type(cities_n_countries))

print('-'* 15)
# interchange keys and values
res = dict((v,k) for k,v in cities_n_countries.items())
print(res)  # NOTE: works only if it follow dit key rules


# # print {'a':2} + {1:'e'}
# TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
