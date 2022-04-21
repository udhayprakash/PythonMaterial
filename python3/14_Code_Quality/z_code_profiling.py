import cProfile

data_list = list(range(10_000_000))
cProfile.run("9_999_999 in data_list")


data_set = set(range(10_000_000))
cProfile.run("9_999_999 in data_set")


# But, creating a set is a bit slower than creating a list
print("CREATING A LIST")
cProfile.run("list(range(10_000_000))")

print("CREATING A SET")
cProfile.run("set(range(10_000_000))")
