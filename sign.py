import sys, binascii, hashlib
from Crypto.Cipher import AES
import key_provider

SECRET_KEY = key_provider.enc_key
HASH_KEY = key_provider.hash_key

key = sys.argv[1]
message = sys.argv[2]


def main():
    signed_message = None
    cipher = AES.new(key, AES.MODE_ECB)
    enc = cipher.encrypt(message).encode('hex')
    for i in range(0, len(key)):
        if key[i] != SECRET_KEY[i]:
            return sys.stderr.write("Key is invalid!")
        # Comply with NIST requirements - 128-bit key and 100,000 iterations
        signed_message = hashlib.pbkdf2_hmac('sha512', enc, HASH_KEY, 100000)

    sys.stdout.write(str(binascii.hexlify(signed_message)))


main()

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
