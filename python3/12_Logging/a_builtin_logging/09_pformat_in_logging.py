#!/usr/bin/python
import logging
from pprint import pformat, pprint

data = [
    (1, {"a": "A", "b": "B", "c": "C", "d": "D"}),
    (
        2,
        {
            "e": "E",
            "f": "F",
            "g": "G",
            "h": "H",
            "i": "I",
            "j": "J",
            "k": "K",
            "l": "L",
        },
    ),
]

print(data)
print()
pprint(data)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)-8s %(message)s",
    filename="logs/09_logging.log",
    filemode="w",
)

logging.debug(data)
logging.debug("Logging pformatted data")

formatted = pformat(data)
for line in formatted.splitlines():
    logging.debug(line.rstrip())
