#!/usr/bin/python3

import click


@click.command()
@click.option("-s", "--string")
def output(string):
    click.echo(string)


if __name__ == "__main__":
    output()

"""
    ~py f_option_names.py

    ~py f_option_names.py -s udhay
    udhay
    ~py f_option_names.py --string udhay
    udhay

    ~py f_option_names.py --help
    Usage: f_option_names.py [OPTIONS]

    Options:
    -s, --string TEXT
    --help             Show this message and exit.

"""
