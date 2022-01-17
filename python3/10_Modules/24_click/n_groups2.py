#!/usr/bin/python3

import click


@click.group()
def cli():
    pass


@cli.command(name='gen')
def generic():
    click.echo('Hello there')


@cli.command(name='wel')
def welcome():
    click.echo('Welcome')


if __name__ == '__main__':
    cli()

"""
USAGE:
    ~py n_groups2.py gen
    Hello there
    ~py n_groups2.py wel
    Welcome

"""
