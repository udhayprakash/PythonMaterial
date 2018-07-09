import argparse

# Arguments
# ex1: --verbose
# ex2: --verbose 4

parser = argparse.ArgumentParser()
parser.add_argument("--verbose",
                    help="increase output verbosity",
                    action="store_true"
                    )

args = parser.parse_args()

if args.verbose:
    print "verbosity turned on"
