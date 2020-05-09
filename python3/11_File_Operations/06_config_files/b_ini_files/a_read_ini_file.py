#!/usr/bin/python
"""
Purpose: Parsing an ini file
"""
from configparser import ConfigParser

parser = ConfigParser()
parser.read('simple.ini')

print(parser.get('bug_tracker', 'url'))
