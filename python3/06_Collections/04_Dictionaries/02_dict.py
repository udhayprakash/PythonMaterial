# ways of creating dictionary 
a = {'one': 1, 'two': 2, 'three': 3}

b = dict(one=1, two=2, three=3)

c = dict([('two', 2), ('one', 1), ('three', 3)])

d = dict(
    zip(['one', 'two', 'three'], [1, 2, 3])
)

e = dict({'three': 3, 'one': 1, 'two': 2})

assert a == b == c == d == e

# ############
data = [(1, 'red'), (2, 'blue'), (3, 'yellow')]
print(dict(data))

data = [('red', 1), ('blue', 2), ('yellow', 3)]
print(dict(data))

data = (('red', 1), ('blue', 2), ('yellow', 3))
print(dict(data))

# data = (['red', 1], ['blue', 2], ('yellow', 3))
# print(dict(data))

# # data = (['red', 1, 'A'], ['blue', 2, 'B'], ('yellow', 3, "C"))
# # print(dict(data))   # ValueError:

# data = (['red',( 1, 'A')], ['blue',( 2, 'B')], ('yellow', (3, "C")))
# print(dict(data))
# ##################
cities = ('New York', 'Shangai', 'New Delhi')
countries = {'US', 'China'}

# list of tuples
print('\n', list(zip(cities, countries)))

cities_n_countries = dict(zip(countries, cities))

print('\ncities_n_countries\n', cities_n_countries)
print(type(cities_n_countries))

print('-' * 15)
print('\ndicts')
for i in cities_n_countries:
    print(i)

print('\ndicts.keys()')
for i in cities_n_countries.keys():
    print(i)

print('\ndicts.values()')
for i in cities_n_countries.values():
    print(i)

print('\ndicts.items()')
for i in cities_n_countries.items():
    print(i, type(i))

a, b = 12, 23
# a, b, c = 12, 23 # ValueError: not enough values to unpack (expected 3, got 2)
a, b, c = 12, 23, 45
a = 12, 23, 45     # tuple
print()
for k, v in cities_n_countries.items():
    print(k, '--->', v)

# interchange keys and values
reverse_dict = {}
for k, v in cities_n_countries.items():
    # reverse_dict[k] = v
    reverse_dict[v] = k

print(f'reverse_dict={reverse_dict}')

res = dict([(v, k) for k, v in cities_n_countries.items()])
print(res)  # NOTE: works only if it follow dit key rules

res = {v: k for k, v in cities_n_countries.items()}
print(res)  # NOTE: works only if it follow dit key rules
