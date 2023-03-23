import objgraph

# print(dir(objgraph))
objgraph.show_most_common_types()
print()


def my_leaky_func():
    pass


# Start counting
objgraph.show_growth(limit=10)

my_leaky_func()

# Stop and show change
objgraph.show_growth(limit=10)
