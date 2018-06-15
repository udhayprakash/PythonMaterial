import string
from random import choice, randint

print 'string.ascii_letters :', string.ascii_letters
print 'string.digits        :', string.digits
print 'string.punctuation   :', string.punctuation

characters = string.ascii_letters + string.punctuation \
                                                + string.digits
password = "".join(choice(characters) 
                        for x in range(randint(8, 16)))
print 'password             :', password
