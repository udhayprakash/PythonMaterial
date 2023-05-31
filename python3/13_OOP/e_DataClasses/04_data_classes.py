import random
from dataclasses import dataclass, field


def random_price():
    return random.randint(20, 100)


@dataclass
class Book(object):
    title: str
    author: str
    price: float = field(default_factory=random_price)


b = Book("Python programming", "David Beazley")
print(vars(b))

b = Book("Python programming", "David Beazley")
print(vars(b))

# Note that you cannot both set default_factory
# and a default value; the whole point is that
# default_factory lets you run a function and,
# thus, provides the value dynamically, when the new instance is created.
