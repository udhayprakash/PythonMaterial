#!/usr/bin/python3

import click


@click.command()
@click.argument('word')
@click.option('--shout/--no-shout', default=False)
def output(word, shout):
    if shout:
        click.echo(word.upper())
    else:
        click.echo(word)


if __name__ == '__main__':
    output()
"""
USAGE:
    ~py i_flags2.py udhay
    udhay

    ~py i_flags2.py --shout udhay
    UDHAY

    ~py i_flags2.py --no-shout udhay
    udhay

"""
