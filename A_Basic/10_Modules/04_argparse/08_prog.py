import argparse

# Arguments
# ex1: 4
# ex2: 4 -v
# ex3: 4 -v 1
# ex4: 4 -v 2
parser = argparse.ArgumentParser()
parser.add_argument("square",
                    type=int,
                    help="display a square of a given number"
                    )

parser.add_argument("-v",
                    "--verbosity",
                    type=int,
                    help="increase output verbosity"
                    )

args = parser.parse_args()
answer = args.square ** 2

if args.verbosity == 2:
    print "the square of {} equals {}".format(args.square, answer)
elif args.verbosity == 1:
    print "{}^2 == {}".format(args.square, answer)
else:
    print answer
