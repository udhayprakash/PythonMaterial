import cProfile

domain = range(50_000)

def example_list():
    data_list = list(domain)
    for i in domain:
        assert i in data_list
        
print("example_list()====")
cProfile.run('example_list()')

def example_set():
    data_set = set(domain)
    for i in domain:
        assert i in data_set

print("example_set()====")
cProfile.run('example_set()')