import argparse

parser = argparse.ArgumentParser(description="Person Details")

parser.add_argument("-n", "--name", required=True)  # defaut type is str
parser.add_argument("-a", "--age", type=int, default=18)

args = parser.parse_args()

print(f"Hello {args.name}, you are {args.age} years old.")
