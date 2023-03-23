#!/usr/bin/python3

import click


@click.command()
@click.option("--name", prompt="Your name", help="Provide your name")
def hello(name):
    click.echo(f"Hello, {name}")


if __name__ == "__main__":
    hello()

"""
USAGE:
    ~py g_prompt.py
    Your name: udhay
    Hello, udhay
    ~py g_prompt.py --helpUsage: g_prompt.py [OPTIONS]

    Options:
    --name TEXT  Provide your name
    --help       Show this message and exit.

"""
