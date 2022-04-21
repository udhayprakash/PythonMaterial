#!/usr/bin/python3

import click


@click.command()
@click.argument('name', default='guest')
@click.argument('age', type=int)
def hello(name, age):
    click.echo(f'{name} is {age} years old')


if __name__ == '__main__':
    hello()

"""
USAGE:
    ~py c_argument_type.py --help
    Usage: c_argument_type.py [OPTIONS] [NAME] AGE
    Options:
    --help  Show this message and exit.
    ~py c_argument_type.py udhay 25
    udhay is 25 years old

    ~py c_argument_type.py udhay
    Usage: c_argument_type.py [OPTIONS] [NAME] AGE
    Try 'c_argument_type.py --help' for help.

    Error: Missing argument 'AGE'.

"""
