#!/usr/bin/python
"""
Purpose: argparse

    nargs keyword can also accept the following:
        ?: a single value, which can be optional
        *: a flexible number of values, which will be gathered into a list
        +: like *, but requiring at least one value
        argparse.REMAINDER: all the values that are remaining in the command line
"""
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('input',  # like sys.argv
                       action='store',
                       nargs='?',
                       default='my default value')

args = my_parser.parse_args()

print(args.input)