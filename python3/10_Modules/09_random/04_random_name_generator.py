from random import choice


def random_name_generator(first, second, x):
    """
    Generates random names.
    Arguments:
     - list of first names
     - list of last names
     - number of random names
    """
    names = []
    for i in range(x):
        names.append(f"{choice(first)} {choice(second)}")
    return set(names)


first_names = ["Drew", "Mike", "Landon", "Jeremy", "Tyler", "Tom", "Avery"]
last_names = ["Smith", "Jones", "Brighton", "Taylor"]
names = random_name_generator(first_names, last_names, 5)
print("\n".join(names))

# Assignment:
# In runtime, take the gender name as input, and generate random name.
# HINT: Take a dataset of female first names, and another with male first names
# one dataset with last names
