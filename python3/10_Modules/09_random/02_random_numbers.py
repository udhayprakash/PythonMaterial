import secrets

"""
Purpose: demonstration of random module

    Python random module, uses pseudo-random generator (PRNG)
    called the Mersenne Twister.
"""
# Pick a random number between 1 and 100.
print(secrets.SystemRandom().randint(1, 100))  # 75
# randint also includes the upper bound value

# Pick a random floating point number between 1 and 10
# random.uniform(a,b) => a <= N <= b
print(secrets.SystemRandom().uniform(1, 10))

# Generate a randomly selected element from range(start, stop, step)
# random.randrange(start, stop[, step])
for i in range(3):
    print(secrets.SystemRandom().randrange(0, 101, 5))


items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Pick a random item from the list
x = secrets.SystemRandom().sample(items, 1)
print(x)
# Pick 4 random items from the list
y = secrets.SystemRandom().sample(items, 4)
print(y)

mountains = ["Andes", "Himalayas", "Alphes", "Aplachein", "Ural", "Vindhya"]

# Pick a random item from the list
x = secrets.SystemRandom().sample(mountains, 1)
print(x[0])

# Pick 3 random items from the list
y = secrets.SystemRandom().sample(mountains, 3)
print(y)

# Pick a random item from the list
x = secrets.choice(mountains)
print(x)
print()


# To shuffle a list of elements
def shuffler(mylist):
    new_list = []
    while len(mylist):
        rand_pos = secrets.SystemRandom().randint(0, len(mylist))
        new_list.append(mylist[rand_pos])
        del mylist[rand_pos]
    return new_list


print(shuffler(["a", "b", "c", "d", "e"]))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
secrets.SystemRandom().shuffle(numbers)
print("after shuffle", numbers)
