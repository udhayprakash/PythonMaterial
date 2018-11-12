

colors = {
    1 :'red', 
    '2' : ['blue', 'bluish green'],
    (3.887, 2) : 'yellow'}

print colors

print '\ncolors.values()', colors.values()

print '\ncolors.keys()  ', colors.keys()
print '\ncolors.items() ', colors.items()

data = [(1, 'red'), (2, 'blue'), (3, 'yellow')]
print dict(data)


cities = ('New York', 'Shangai', 'New Delhi')
countries = {'US', 'China'}

# list of tuples
print zip(cities, countries)

cities_n_countries = dict(
    zip(countries, cities)
    )

print '\ncities_n_countries\n', cities_n_countries
print type(cities_n_countries)

print '-'* 15
# list of tuples
print map(None, cities, countries)

cities_n_countries = dict(
    map(None,countries, cities)
    )

print '\ncities_n_countries\n', cities_n_countries
print type(cities_n_countries)

# # print cities_n_countries['china']
# print cities_n_countries.get('china')
# print cities_n_countries.get('china', None)
# print cities_n_countries.get('china', 'NO such key')
# print cities_n_countries.get('china', 666)
