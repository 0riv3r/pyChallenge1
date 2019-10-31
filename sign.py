import sys, base64, binascii, hashlib
from Crypto.Cipher import AES
from Crypto import Random
import key_provider
secret_key = key_provider.enc_key
hash_key = key_provider.hash_key

key = sys.argv[1]
message = sys.argv[2]

def sign(key, message):
    C = AES.new(key, AES.MODE_ECB)
    enc = C.encrypt(message).encode('hex')
    for i in range(0, len(key)):
        if key[i] != secret_key[i]:
            return "Key is invalid!"
        # NIST approved 128-bit salt and 100,000 iterations
        output = hashlib.pbkdf2_hmac('sha512', enc, hash_key, 100000)

    return "Signed Message:", binascii.hexlify(output)

print sign(key, message)

###############################################################

# Python 2.7.17rc1

# python sign.py 7781c66d36dc3a22447a6e5bf8c89090 "Message_to_sign!"

# Setup
# -----
# sudo apt search python-dev
# then may be
# sudo apt install python-dev
# sudo apt install libpython-dev
# sudo apt install python-setuptools
# sudo apt install python-pip
# pip install pycrypto



