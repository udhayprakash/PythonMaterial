import secrets 
print(dir(secrets))

print(secrets.choice([1, 2, 3, 4]))
print(secrets.choice('Udhay'))
# Return a randomly-chosen element from a non-empty sequence.

print(secrets.randbelow(8))
# Return a random int in the range [0, n).

print(secrets.randbits(8))
# Return an int with k random bits.

print(secrets.token_bytes(nbytes=10))
# Return a random byte string containing nbytes number of bytes. If nbytes is None or not supplied, a reasonable default is used.

print(secrets.token_hex(nbytes=10))
# Return a random text string, in hexadecimal. The string has nbytes random bytes, each byte converted to two hex digits. If nbytes is None or not supplied, a reasonable default is used.

print(secrets.token_urlsafe(nbytes=10))
# Return a random URL-safe text string, containing nbytes random bytes. The text is Base64 encoded, so on average each byte results in approximately 1.3 characters. If nbytes is None or not supplied, a reasonable default is used.


##################################
sec_gen = secrets.SystemRandom()
print(dir(sec_gen)) 

print(sec_gen.randint(0,50))
# random integer number uisng secrets

print(sec_gen.randrange(4, 40, 4))
# random integer number within given range using secrets

print(sec_gen.uniform(2.5, 25.5))
# Secure Random uniform using secrets

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sec_gen.sample(number_list, 3))
print(sec_gen.sample(number_list, 1))
# Secure Random sample using secrets

print(sec_gen.choice(number_list))

sec_gen.shuffle(number_list)
print(number_list)



