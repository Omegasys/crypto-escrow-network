from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

class AES256:
    def __init__(self, key_size=32, block_size=16):
        self.key_size = key_size
        self.block_size = block_size
        self.key = None
        self.iv = None

    def generate_key(self):
        self.key = get_random_bytes(self.key_size)
        return self.key

    def generate_iv(self):
        self.iv = get_random_bytes(self.block_size)
        return self.iv

    def encrypt(self, plaintext):
        cipher = AES.new(self.key, AES.MODE_CBC, iv=self.iv)
        ciphertext = cipher.encrypt(pad(plaintext, self.block_size))
        return ciphertext

    def decrypt(self, ciphertext):
        cipher = AES.new(self.key, AES.MODE_CBC, iv=self.iv)
        plaintext = unpad(cipher.decrypt(ciphertext), self.block_size)
        return plaintext
