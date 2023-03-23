import click


@click.command()
def hello():
    click.echo("Hello there")


if __name__ == "__main__":
    hello()


# USAGE:
#     python a_simple.py --help
