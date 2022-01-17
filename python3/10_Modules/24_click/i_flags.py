#!/usr/bin/python3

import click


@click.command()
@click.option('--blue', is_flag=True, help='message in blue color')
def hello(blue):
    if blue:
        click.secho('Hello there', fg='blue')
    else:
        click.secho('Hello there')


if __name__ == '__main__':
    hello()

"""
USAGE:
    ~py i_flags.py
    Hello there
    ~py i_flags.py --help
    Usage: i_flags.py [OPTIONS]
    Options:
    --blue  message in blue color
    --help  Show this message and exit.

    ~py i_flags.py --blue
    Hello there

"""
