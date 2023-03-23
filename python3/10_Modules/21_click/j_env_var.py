#!/usr/bin/python3

import os

import click

os.environ["MYDIR"] = "."  # or set this env variable


@click.argument("mydir", envvar="MYDIR", type=click.Path(exists=True))
@click.command()
def dolist(mydir):
    print(f"{mydir=}")
    click.echo(os.listdir(mydir))


if __name__ == "__main__":
    dolist()
