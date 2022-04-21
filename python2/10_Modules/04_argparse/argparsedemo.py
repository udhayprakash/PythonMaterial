import argparse

def main(m, n, p):
    """ Short script to add three numbers """
    return m + n + p


# print '__name__', __name__

# if __name__ == '__main__':
parser = argparse.ArgumentParser(
    description='Script to add three numbers')
parser.add_argument('-a',
                    help='First value',
                    type=float,
                    default=0)
parser.add_argument('-b',
                    help='Second value',
                    type=float,
                    required=True)
parser.add_argument('-c',
                    help='Third value',
                    type=int)
args = parser.parse_args()

print 'type(args.a)', type(args.a)
print 'type(args.b)', type(args.b)
print 'type(args.c)', type(args.c)


print(main(args.a, args.b, args.c))
