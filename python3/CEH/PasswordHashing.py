import bcrypt
import base64
import hashlib

password = b"super secret password"
# Hash a password for the first time, with a randomly-generated salt
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
# Check that an unhashed password matches one that has previously been
# hashed
if bcrypt.checkpw(password, hashed):
    print("It Matches!")
else:
    print("It Does not Match :(")

"""
Maximum Password Length 
-----------------------
"bcrypt algorithm only handles passwords up to 72 characters, any characters beyond that are ignored. 
To work around this, a common approach is to hash a password with a cryptographic hash (such as sha256) 
and then base64 encode it to prevent NULL byte problems before hashing the result with bcrypt"

"""

password = b"an incredibly long password" * 10
hashed = bcrypt.hashpw(
    base64.b64encode(hashlib.sha256(password).digest()),
    bcrypt.gensalt()
)

print
'hashed:', hashed
