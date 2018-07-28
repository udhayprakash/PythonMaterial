import argparse

def main(m, n, p):
    """ Short script to add three numbers """
    return m + n + p


# print '__name__', __name__

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Add three numbers")
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
                        type=float)
    args = parser.parse_args()
    print(main(args.a, args.b, args.c))
