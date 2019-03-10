from math import sqrt
print(list(map(sqrt, (4, 16, 25))))
print(list(map(sqrt, [4])))
# print map(sqrt, 4)TypeError: argument 2 to map() must support iteration


# Improving the above with decorators

def elementwise(fn):
    def newfn(arg):
        if hasattr(arg,'__getitem__'):  # is a Sequence
            return type(arg)(list(map(fn, arg)))
        else:
            return fn(arg)
    return newfn
 
@elementwise
def compute(x):
    return x**3 - 1
 
print(compute(5))        # prints: 124
print(compute([1,2,3]))  # prints: [0, 7, 26]
print(compute((1,2,3)))  # prints: (0, 7, 26)