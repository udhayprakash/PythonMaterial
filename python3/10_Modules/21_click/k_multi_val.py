#!/usr/bin/python3

import click


@click.command()
@click.option("--data", required=True, type=(str, int))
def output(data):
    click.echo(f"name={data[0]} age={data[1]}")


if __name__ == "__main__":
    output()
"""
USAGE:
    ~py k_multi_val.py --data udhay 25
    name=udhay age=25
    ~py k_multi_val.py --help
    Usage: k_multi_val.py [OPTIONS]
    Options:
    --data <TEXT INTEGER>...  [required]
    --help                    Show this message and exit.
"""
