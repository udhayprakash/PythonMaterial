#!/usr/bin/python3

import click


@click.group()
def messages():
    pass


@click.command()
def generic():
    click.echo('Hello there')


@click.command()
def welcome():
    click.echo('Welcome')


messages.add_command(generic)
messages.add_command(welcome)


if __name__ == '__main__':
    messages()

"""
USAGE:
    ~py n_groups.py generic
    Hello there
    ~py n_groups.py welcome
    Welcome
    ~py n_groups.py        
    Usage: n_groups.py [OPTIONS] COMMAND [ARGS]...

    Options:
    --help  Show this message and exit.

    Commands:
    generic
    welcome

"""