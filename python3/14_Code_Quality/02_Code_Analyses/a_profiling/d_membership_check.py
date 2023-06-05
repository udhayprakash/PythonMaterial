import cProfile

domain = range(50_000)


def example_list():
    data_list = list(domain)
    for i in domain:
        assert i in data_list  # O(N)


print("example_list()====")
cProfile.run("example_list()")  # 20.369 seconds
print()


def example_set():
    data_set = set(domain)
    for i in domain:
        assert i in data_set  # O(1)


print("example_set()====")
cProfile.run("example_set()")  # 0.007 seconds
