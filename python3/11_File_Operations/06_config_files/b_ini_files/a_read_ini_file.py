#!/usr/bin/python
"""
Purpose: Parsing an ini file

In python 2.x, configParser
In python 3.x, configparser
"""
from configparser import ConfigParser

parser = ConfigParser()
parser.read('simple.ini')

print(parser.get('bug_tracker', 'url'))
#                 section        key
