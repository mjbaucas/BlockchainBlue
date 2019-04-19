import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

class AESCipher:
    def __init__(self):
        self.base = 32

    def encrypt(self, secret, key):
        key = hashlib.sha256(key.encode()).digest()
        secret = str(secret) + (self.base - len(secret) % self.base) * chr(self.base - len(secret) % self.base)
        init_vec = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CFB, init_vec)
        return base64.b64encode(init_vec + cipher.encrypt(secret))

    def decrypt(self, encrypted, key):
        key = hashlib.sha256(key.encode()).digest()
        encrypted = base64.b64decode(encrypted)
        init_vec = encrypted[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CFB, init_vec)
        secret = cipher.decrypt(encrypted[AES.block_size:])
        return secret[:-ord(secret[len(secret)-1:])]
