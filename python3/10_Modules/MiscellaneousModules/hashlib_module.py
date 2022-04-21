import hashlib

print(dir(hashlib))

hashlib.algorithms_available
# {'blake2b',
#  'blake2s',
#  'md4',
#  'md5',
#  'md5-sha1',
#  'mdc2',
#  'ripemd160',
#  'sha1',
#  'sha224',
#  'sha256',
#  'sha384',
#  'sha3_224',
#  'sha3_256',
#  'sha3_384',
#  'sha3_512',
#  'sha512',
#  'sha512_224',
#  'sha512_256',
#  'shake_128',
#  'shake_256',
#  'sm3',
#  'whirlpool'}

hashlib.algorithms_guaranteed
# {'blake2b',
#  'blake2s',
#  'md5',
#  'sha1',
#  'sha224',
#  'sha256',
#  'sha384',
#  'sha3_224',
#  'sha3_256',
#  'sha3_384',
#  'sha3_512',
#  'sha512',
#  'shake_128',
#  'shake_256'}

# hashlib.sha1('Apple')
# TypeError: Unicode-objects must be encoded before hashing


hashlib.sha1(b"Apple")  # <sha1 HASH object @ 0x000001E8D1660550>
hashlib.sha1(b"Apple").hexdigest()  # '476432a3e85a0aa21c23f5abd2975a89b6820d63'
hashlib.sha256(
    b"Apple"
).hexdigest()  # 'f223faa96f22916294922b171a2696d868fd1f9129302eb41a45b2a2ea2ebbfd'
hashlib.md5(b"Apple").hexdigest()  # '9f6290f4436e5a2351f12e03b6433c3c'
