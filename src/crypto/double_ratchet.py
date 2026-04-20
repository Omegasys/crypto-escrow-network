import os
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from Crypto.Random import get_random_bytes
from hashlib import sha256

class DoubleRatchet:
    def __init__(self, key_size=32, message_key_size=32):
        self.key_size = key_size
        self.message_key_size = message_key_size
        self.root_key = None
        self.chain_key = None
        self.message_key = None
        self.sending_chain_key = None
        self.receiving_chain_key = None

    def generate_root_key(self):
        self.root_key = get_random_bytes(self.key_size)
        return self.root_key

    def derive_chain_keys(self):
        # Use scrypt or HKDF to derive chain keys from the root key
        self.chain_key = scrypt(self.root_key, b"chain", 32, N=2**14, r=8, p=1)
        self.sending_chain_key = self.chain_key
        self.receiving_chain_key = self.chain_key

    def generate_message_key(self, chain_key):
        # Deriving a message key from the chain key
        message_key = sha256(chain_key).digest()[:self.message_key_size]
        return message_key

    def encrypt_message(self, plaintext):
        message_key = self.generate_message_key(self.sending_chain_key)
        cipher = AES.new(message_key, AES.MODE_CBC)
        iv = cipher.iv
        ciphertext = cipher.encrypt(plaintext)
        return iv + ciphertext

    def decrypt_message(self, ciphertext):
        message_key = self.generate_message_key(self.receiving_chain_key)
        iv = ciphertext[:16]  # Assuming 16-byte IV
        cipher = AES.new(message_key, AES.MODE_CBC, iv=iv)
        plaintext = cipher.decrypt(ciphertext[16:])
        return plaintext
