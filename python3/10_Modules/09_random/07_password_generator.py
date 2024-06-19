import string
import secrets

print("string.ascii_letters :", string.ascii_letters)
print("string.digits        :", string.digits)
print("string.punctuation   :", string.punctuation)

characters = string.ascii_letters + string.punctuation + string.digits
password1 = "".join(secrets.choice(characters) for x in range(secrets.SystemRandom().randint(8, 16)))
print("password1             :", password1)

password2 = "".join(secrets.choice(characters) for x in range(secrets.SystemRandom().randrange(8, 16)))
print("password2             :", password2)


print(
    "".join(secrets.SystemRandom().sample(string.ascii_letters, 4))
    + "".join(secrets.SystemRandom().sample(string.digits, 4))
    + "".join(secrets.SystemRandom().sample(string.punctuation, 4))
)
