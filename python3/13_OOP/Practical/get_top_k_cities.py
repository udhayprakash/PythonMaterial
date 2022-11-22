"""
Problem:
    Design and implement a method which returns the top K cities for a given weather attribute.

Possible Attributes:
- Pressure
- Humidity
- Temp

Fields Representing a City:
- Id
- Name
- Temp
- Pressure
- Humidity

Your method should take a list of objects representing the cities, the number of cities, and the attribute.
The output should be a list of the top K cities.
"""


class City:
    def __init__(self, id, name, temp, pressure, humidity):
        self.id = id
        self.name = name
        self.temp = temp
        self.pressure = pressure
        self.humidity = humidity

    def __repr__(self):
        return repr(self.name)

    __str__ = __repr__


def get_top(cities, attribute, count):
    if not cities:
        return []
    if not hasattr(cities[0], attribute):
        return Exception("No such attribute")

    cities.sort(key=lambda x: vars(x)[attribute], reverse=True)
    return cities[:count]


result = get_top(
    [
        City(1, "fremont", 34, 23.2, 213.213),
        City(2, "redmont", 56, 343.1, 3),
        City(3, "bayarea", 23, 34, 56),
        City(4, "dallas", 3, 47, 32),
    ],
    "temp",
    2,
)


assert [c.name for c in result] == ["redmont", "fremont"]
