from Crypto.Cipher import ChaCha20
from Crypto.Protocol.KDF import scrypt
from Crypto.Random import get_random_bytes
import hashlib

class ChaCha20Poly1305:
    def __init__(self, key_size=32, nonce_size=12):
        self.key_size = key_size
        self.nonce_size = nonce_size
        self.key = None
        self.nonce = None

    def generate_key(self):
        self.key = get_random_bytes(self.key_size)
        return self.key

    def generate_nonce(self):
        self.nonce = get_random_bytes(self.nonce_size)
        return self.nonce

    def encrypt(self, plaintext, associated_data=None):
        cipher = ChaCha20.new(key=self.key, nonce=self.nonce)
        ciphertext = cipher.encrypt(plaintext)
        
        if associated_data:
            tag = hashlib.sha256(associated_data).digest()
            return ciphertext, tag
        else:
            return ciphertext

    def decrypt(self, ciphertext, associated_data=None):
        cipher = ChaCha20.new(key=self.key, nonce=self.nonce)
        plaintext = cipher.decrypt(ciphertext)
        
        if associated_data:
            tag = hashlib.sha256(associated_data).digest()
            return plaintext, tag
        else:
            return plaintext
