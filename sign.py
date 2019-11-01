import sys, binascii, hashlib
from Crypto.Cipher import AES
import key_provider

secret_key = key_provider.enc_key
hash_key = key_provider.hash_key

key = sys.argv[1]
message = sys.argv[2]


def main():
    signed_message = None
    cipher = AES.new(key, AES.MODE_ECB)
    enc = cipher.encrypt(message).encode('hex')
    for i in range(0, len(key)):
        if key[i] != secret_key[i]:
            return sys.stderr.write("Key is invalid!")
        # NIST approved 128-bit salt and 100,000 iterations
        signed_message = hashlib.pbkdf2_hmac('sha512', enc, hash_key, 100000)

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
