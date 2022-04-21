#!/usr/bin/python3

import click


@click.command()
def coloured():
    click.secho('Hello there', fg='blue', bold=True)


if __name__ == '__main__':
    coloured()


"""
USAGE:
~py h_coloured.py
Hello there

"""
