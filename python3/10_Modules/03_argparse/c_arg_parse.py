#!/usr/bin/python
"""
Purpose: argparse
"""
import argparse

my_parser = argparse.ArgumentParser()


# my_parser.add_argument("--inputvalues", action="store", nargs=3)
my_parser.add_argument("--inputvalues", action="store", nargs=3, type=int)


args = my_parser.parse_args()

print(f"{args.inputvalues =}")
print(f"{type(args.inputvalues)=}")  # list


"""
python c_arg_parse.py
args.inputvalues =None

python c_arg_parse.py --inputvalues 12 13 14
args.inputvalues =[12, 13, 14]
type(args.inputvalues)=<class 'list'>

"""
