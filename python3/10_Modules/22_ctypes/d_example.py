import gc


def deref(id_):
    f = {id(x): x for x in gc.get_objects()}
    return f[id_]


if __name__ == '__main__':
    foo = [1, 2, 3]
    bar = id(foo)
    print(deref(bar))  # [1, 2, 3]
