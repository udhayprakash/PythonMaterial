#!/usr/bin/python
"""
Purpose: argparse
"""
import argparse

my_parser = argparse.ArgumentParser()
# my_parser.add_argument('--input', action='store',  nargs=3)
my_parser.add_argument('--input', action='store', type=int, nargs=3)
# NOTE: expected three values mandatorily

args = my_parser.parse_args()
print(f'{args.input      =}')
print(f'{type(args.input)=}')  # list
