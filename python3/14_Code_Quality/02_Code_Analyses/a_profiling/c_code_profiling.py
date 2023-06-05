import cProfile

data_list = list(range(10_000_000))
cProfile.run("9_999_999 in data_list")  # O(N)


data_set = set(range(10_000_000))
cProfile.run("9_999_999 in data_set")  # O(1)

print()


# But, creating a set is a bit slower than creating a list
print("CREATING A LIST")
cProfile.run("list(range(10_000_000))")  # 0.582 sec

print("CREATING A SET")
cProfile.run("set(range(10_000_000))")  # 1.569 s


"""
NOTE:
    -- When we have MORE reads, go for set/dict
    -- When we have MORE writes, go for List/Tuple/np.array

"""
