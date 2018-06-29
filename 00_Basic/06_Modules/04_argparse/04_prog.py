import argparse

# Positional arguments
parser = argparse.ArgumentParser()
parser.add_argument("square",
                    help="display a square of a given number",
                    type=int  # comment this line and observe
                    )
args = parser.parse_args()

print args.square ** 2
