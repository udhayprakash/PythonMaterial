#!/usr/bin/python3

import click


@click.command()
@click.option('--word', '-w', multiple=True)
def words(word):
    click.echo('\n'.join(word))


if __name__ == '__main__':
    words()


"""
USAGE:

    ~py l_multiples.py  -w sky --word forest --word rock -w cloud
    sky
    forestrock
    cloud

"""
