"""
Purpose: Creating custom iterator class using
  __iter__ and __next__
"""
# mylist = [1, 2, 3, 4, 5]
# print(mylist)

# mylist_iter = iter(mylist)
# print(mylist_iter)
# print(next(mylist_iter))
# print(next(mylist_iter))
# print(next(mylist_iter))
# print()


class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, maximum=0):
        self.maximum = maximum

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.maximum:
            result = 2**self.n
            self.n += 1
            return result
        else:
            raise StopIteration


if __name__ == "__main__":
    output = PowTwo(4)
    print(f"output      :{output}")
    print(f"type(output):{type(output)}")

    output_iter = iter(output)
    print(f"\noutput_iter      :{output_iter}")
    print(f"type(output_iter):{type(output_iter)}")

    print(f"next(output_iter):{next(output_iter)}")
    print(f"next(output_iter):{next(output_iter)}")
    print(f"next(output_iter):{next(output_iter)}")
    print(f"next(output_iter):{next(output_iter)}")
    print(f"next(output_iter):{next(output_iter)}")

    try:
        print(f"next(output_iter):{next(output_iter)}")
    except StopIteration as ex:
        print(repr(ex))

    for each in output_iter:
        print(each)
