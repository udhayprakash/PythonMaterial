#!/usr/bin/python
"""
Purpose: parsing Query parameters string
"""

from urllib.parse import parse_qs
import urllib.parse

my_values = parse_qs("red=5&blue=0&green=", keep_blank_values=True)
print(repr(my_values))  # {'red': ['5'], 'blue': ['0'], 'green': ['']}

print("Red    : ", my_values.get("red"))
print("Green  : ", my_values.get("green"))
print("Opacity: ", my_values.get("opacity"))

# For query string 'red=5&blue=0&green='
red = my_values.get("red", [""])[0] or 0
green = my_values.get("green", [""])[0] or 0
opacity = my_values.get("opacity", [""])[0] or 0
print("Red    : %r" % red)
print("Green  : %r" % green)
print("Opacity: %r" % opacity)


# Encode

params = urllib.parse.urlencode({"spam": 1, "eggs": 2, "bacon": 0})
print(params)  # spam=1&eggs=2&bacon=0
