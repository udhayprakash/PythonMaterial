import random

"""
Purpose: demonstration of random module

    Python random module, uses pseudo-random generator (PRNG)
    called the Mersenne Twister.
"""
# Pick a random number between 1 and 100.
print(random.randint(1, 100))  # 75
# randint also includes the upper bound value

# Pick a random floating point number between 1 and 10
# random.uniform(a,b) => a <= N <= b
print(random.uniform(1, 10))

# Generate a randomly selected element from range(start, stop, step)
# random.randrange(start, stop[, step])
for i in range(3):
    print(random.randrange(0, 101, 5))


items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Pick a random item from the list
x = random.sample(items, 1)
print(x)
# Pick 4 random items from the list
y = random.sample(items, 4)
print(y)

mountains = ["Andes", "Himalayas", "Alphes", "Aplachein", "Ural", "Vindhya"]

# Pick a random item from the list
x = random.sample(mountains, 1)
print(x[0])

# Pick 3 random items from the list
y = random.sample(mountains, 3)
print(y)

# Pick a random item from the list
x = random.choice(mountains)
print(x)
print()


# To shuffle a list of elements
def shuffler(mylist):
    new_list = []
    while len(mylist):
        rand_pos = random.randint(0, len(mylist))
        new_list.append(mylist[rand_pos])
        del mylist[rand_pos]
    return new_list


print(shuffler(["a", "b", "c", "d", "e"]))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(numbers)
print("after shuffle", numbers)
