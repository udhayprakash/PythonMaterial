#!/usr/bin/python3

from functools import reduce
from operator import mul

import click


@click.command()
@click.argument("vals", type=int, nargs=-1)
def process(vals):

    print(f"The sum is {sum(vals)}")
    print(f"The product is {reduce(mul, vals, 1)}")


if __name__ == "__main__":
    process()

"""
USAGE:
    ~py d_variable_args.py --help
    Usage: d_variable_args.py [OPTIONS] [VALS]...

    Options:
    --help  Show this message and exit.

    ~py d_variable_args.py
    The sum is 0
    The product is 1

    ~py d_variable_args.py 1 2 3 4 5
    The sum is 15
    The product is 120

"""
