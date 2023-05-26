#!/usr/bin/python
"""
Purpose: Reading (Parsing) config files

    python 2.x - ConfigParser
    python 3.x - configparser

"""

import configparser

# print(dir(configparser))

config = configparser.RawConfigParser()


config.add_section("Section1")
config.set("Section1", "an_int", "15")
config.set("Section1", "a_bool", "true")
config.set("Section1", "a_float", "3.1415")

config.add_section("Section2")
config.set("Section2", "baz", "fun")
config.set("Section2", "bar", "Python")
config.set("Section2", "foo", "%(bar)s is %(baz)s!")


# Writing our configuration file to 'example.cfg'
with open("example.cfg", "w", encoding="utf-8") as configfile:
    config.write(configfile)
