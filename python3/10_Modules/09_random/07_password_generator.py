import string
from random import choice, randint, randrange, sample

print("string.ascii_letters :", string.ascii_letters)
print("string.digits        :", string.digits)
print("string.punctuation   :", string.punctuation)

characters = string.ascii_letters + string.punctuation + string.digits
password1 = "".join(choice(characters) for x in range(randint(8, 16)))
print("password1             :", password1)

password2 = "".join(choice(characters) for x in range(randrange(8, 16)))
print("password2             :", password2)


print(
    "".join(sample(string.ascii_letters, 4))
    + "".join(sample(string.digits, 4))
    + "".join(sample(string.punctuation, 4))
)
