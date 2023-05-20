import random


def random_name_generator(first, second, count):
    _names = []
    for _ in range(count):
        fst_name = random.choice(first)
        lst_name = random.choice(second)
        name = f"{fst_name} {lst_name}"
        _names.append(name)
    return _names


def random_name_generator(first, second, count):
    _names = set()
    while len(_names) < count:
        fst_name = random.choice(first)
        lst_name = random.choice(second)
        name = f"{fst_name} {lst_name}"
        _names.add(name)
    return _names


first_names = ["Drew", "Mike", "Landon", "Jeremy", "Tyler", "Tom", "Avery"]
last_names = ["Smith", "Jones", "Brighton", "Taylor"]
names = random_name_generator(first_names, last_names, 5)
print("\n".join(names))


# Assignment:
# In runtime, take the gender name as input, and generate random name.
# HINT: Take a dataset of female first names, and another with male first names
# one dataset with last names
