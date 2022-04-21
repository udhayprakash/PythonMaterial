#!/usr/bin/python3

import click


@click.command()
@click.argument('name', default='guest')
def hello(name):
    click.echo(f'Hello {name}')


if __name__ == '__main__':
    hello()


"""
USAGE:
    ~py b_arguments.py --help
    Usage: b_arguments.py [OPTIONS] [NAME]
    Options:  --help  Show this message and exit.

    ~py b_arguments.py
    Hello guest

    ~py b_arguments.py udhay
    Hello udhay


"""
