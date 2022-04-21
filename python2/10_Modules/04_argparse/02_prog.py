import argparse

# Positional arguments
parser = argparse.ArgumentParser()
parser.add_argument('echo')
args = parser.parse_args()
print args.echo
