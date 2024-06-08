# server/service/encryption.py
import base64

KEY = "supersecretkey"


def encrypt(message):
    return base64.b64encode(xor_encrypt(message, KEY).encode()).decode()


def decrypt(encrypted_message):
    return xor_encrypt(base64.b64decode(encrypted_message).decode(), KEY)


def xor_encrypt(message, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(message))
