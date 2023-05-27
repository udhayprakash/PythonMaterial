"""
Purpose: Parsing an ini file

In python 2.x, configParser
In python 3.x, configparser
"""
import configparser

parser = configparser.ConfigParser()
parser.read("simple.ini")

# print(dir(parser))


url = parser.get("bug_tracker", "url")
#                 section        key

print(url)
