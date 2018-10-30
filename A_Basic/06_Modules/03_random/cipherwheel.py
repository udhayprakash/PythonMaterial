#cipherwheel.py
import string
from random import randrange

#functions for encryption and decryption

def encrypt(m):
    #define circular wheels
    inner_wheel = [i for i in string.lowercase]
    outer_wheel = inner_wheel
    #caluclate random secret key
    while True:
        key = randrange(26)
        if key!=0:
            break
    cipher_dict={}
    #map the encryption logic
    original_key =key
    for i in range(26):
        cipher_dict[outer_wheel[i]] = inner_wheel[key%26]
        key = key+1
    #getting encrypted message
    print 'Encrypted with secret key ->> %d\n'%original_key
    cipher = ''.join([cipher_dict[i] if i!=' ' else ' ' for i in m])
    return cipher,original_key

def decrypt(cipher,key):
    inner_wheel = [i for i in string.lowercase]    
    outer_wheel = inner_wheel
    cipher_dict={}
    for i in range(26):
        cipher_dict[outer_wheel[i]] = inner_wheel[key%26]
        key = key+1
    #decryption logic
    reverse_dict = dict(zip(cipher_dict.values() , cipher_dict.keys()))

    #getting original message back
    message = ''.join([reverse_dict[i] if i!=' ' else ' ' for i in cipher])
    return message

#Using cipher wheel here


while True:
    s = raw_input("Enter your secret message:")
    encrypted = encrypt(s)
    print 'encrypted message ->> %s\n'%(encrypted[0])
    print 'decrypted message ->> %s\n'%decrypt(encrypted[0],encrypted[1])