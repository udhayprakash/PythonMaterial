from collections import defaultdict
from pprint import pprint

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favourite_colours = defaultdict(list)

for name, colour in colours:
    favourite_colours[name].append(colour)

pprint(favourite_colours)

favourite_colours = defaultdict(set)

for name, colour in colours:
    favourite_colours[name].add(colour)

pprint(favourite_colours)