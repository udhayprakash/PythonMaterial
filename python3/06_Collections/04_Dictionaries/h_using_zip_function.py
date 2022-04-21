#!/usr/bin/python3
"""
Purpose: ways of defining dictionaries
"""
from pprint import pprint

# ways of creating dictionary
a = {"one": 1, "two": 2, "three": 3}
b = dict(one=1, two=2, three=3)
c = dict([("two", 2), ("one", 1), ("three", 3)])
d = dict(zip(["one", "two", "three"], [1, 2, 3]))
e = dict({"three": 3, "one": 1, "two": 2})

assert a == b == c == d == e

# creating dict from pairs
data = [(1, "red"), (2, "blue"), (3, "yellow")]
print(dict(data))

data = [("red", 1), ("blue", 2), ("yellow", 3)]
print(dict(data))

data = (("red", 1), ("blue", 2), ("yellow", 3))
print(dict(data))

data = (["red", 1], ["blue", 2], ("yellow", 3))
print(dict(data))

# data = (['red', 1, 'A'], ['blue', 2, 'B'], ('yellow', 3, "C"))
# print(dict(data))
# ValueError: dictionary update sequence element #0 has length 3; 2 is required


data = (["red", (1, "A")], ["blue", (2, "B")], ("yellow", (3, "C")))
print(dict(data))

data = ([("red", 1), "A"], [("blue", 2), "B"], ("yellow", (3, "C")))
print(dict(data))

# -----------------------

# creating a dict from two iterables
print()
cities = ("New Delhi", "New York", "Shangai", "Berlin")
# countries = {'India', 'USA', 'China', 'Germany'}
# NOTE: never take as a set, as order is not preserved

countries = ["India", "USA", "China", "Germany"]

print(zip(cities, countries))  # <zip object at 0x000001D5472BE740>
# zip - lazy execution


print(list(zip(cities, countries)))


cities_n_countries = dict(zip(cities, countries))
pprint(cities_n_countries)


counties_n_cities = dict(zip(countries, cities))
pprint(counties_n_cities)
print()


print(dict(zip("Python", range(6))))
print(dict(zip("Python", "fish")))


# Question: How to interchange keys with values in dict
print()
my_dict = dict(zip((1, 2, 3, 4), "abcdef"))
print(my_dict)

# question - How to reverse the key -values as values-keys
reverse_dict = {}
for each_key, each_value in my_dict.items():
    # print(f"{each_key =} \t {each_value =}")
    # reverse_dict[each_key] = each_value
    reverse_dict[each_value] = each_key

print(reverse_dict)
