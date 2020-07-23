
data = [(1, 'red'), (2, 'blue'), (3, 'yellow')]
print dict(data)

data = [('red', 1), ('blue', 2), ('yellow', 3)]
print dict(data)

cities = ('New York', 'Shangai', 'New Delhi')
countries = {'US', 'China'}

# list of tuples
print '\n', zip(cities, countries)

cities_n_countries = dict(    zip(countries, cities)    )

print '\ncities_n_countries\n', cities_n_countries
print type(cities_n_countries)

print '-'* 15
# list of tuples
print map(None, cities, countries)

cities_n_countries = dict(    map(None,countries, cities)    )

print '\ncities_n_countries\n', cities_n_countries
print type(cities_n_countries)

# # print cities_n_countries['china']
# print cities_n_countries.get('china')
# print cities_n_countries.get('china', None)
# print cities_n_countries.get('china', 'NO such key')
# print cities_n_countries.get('china', 666)


# print {'a':2} + {1:'e'}
# TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
