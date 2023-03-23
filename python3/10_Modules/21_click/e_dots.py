#!/usr/bin/python3

import click


@click.command()
@click.option("--n", type=int, default=1)
def dots(n):
    click.echo("." * n)


if __name__ == "__main__":
    dots()

"""
USAGE:
    ~py e_dots.py
    .
    ~py e_dots.py 10
    Usage: e_dots.py [OPTIONS]Try 'e_dots.py --help' for help.

    Error: Got unexpected extra argument (10)

    ~py e_dots.py --n 10
    ..........

    ~py e_dots.py --n 5
    .....

"""
