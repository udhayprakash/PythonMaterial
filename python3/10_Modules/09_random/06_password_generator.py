import random

alphabet = "abcdefghijklmnopqrstuvwxyz .,!@_-(*)-+/|$%&=?^"
pw_length = 34  # can change the length of your password by changing this number


mypw = "".join(random.sample(alphabet, pw_length))
print(mypw)
print()

mypw = ""
for i in range(pw_length):
    next_index = random.randrange(len(alphabet))
    mypw += alphabet[next_index]
print(mypw)
print()


# replace 1 or 2 characters with a number
for i in range(random.randrange(1, 3)):
    replace_index = random.randrange(len(mypw) // 2)
    mypw = mypw[0:replace_index] + str(random.randrange(10)) + mypw[replace_index + 1 :]

# replace 1 or 2 letters with an uppercase letter
for i in range(random.randrange(1, 3)):
    replace_index = random.randrange(len(mypw) // 2, len(mypw))
    mypw = (
        mypw[0:replace_index] + mypw[replace_index].upper() + mypw[replace_index + 1 :]
    )

print(mypw)
