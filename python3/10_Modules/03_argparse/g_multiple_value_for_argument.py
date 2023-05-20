# Multiple values for an argument
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--numbers", nargs="+", type=int)
args = parser.parse_args()

print(f"{args.numbers =}")
print(sum(args.numbers))
