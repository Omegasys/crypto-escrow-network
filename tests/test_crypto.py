import unittest
from crypto.chaCha20_poly1305 import ChaCha20Poly1305
from crypto.aes256 import AES256
from crypto.double_ratchet import DoubleRatchet
from utils.encryption_utils import encrypt_data_aes, decrypt_data_aes, generate_rsa_keys

class TestEncryptionProtocols(unittest.TestCase):

    def test_aes_encryption(self):
        data = "Sensitive data"
        key = b'Sixteen byte key'
        encrypted_data = encrypt_data_aes(data, key)
        decrypted_data = decrypt_data_aes(encrypted_data, key)
        self.assertEqual(data, decrypted_data)

    def test_rsa_key_generation(self):
        private_key, public_key = generate_rsa_keys()
        self.assertIsNotNone(private_key)
        self.assertIsNotNone(public_key)

    def test_chaCha20_poly1305_encryption(self):
        cipher = ChaCha20Poly1305()
        data = b"Test message"
        encrypted_data = cipher.encrypt(data)
        decrypted_data = cipher.decrypt(encrypted_data)
        self.assertEqual(data, decrypted_data)

    def test_aes256_encryption(self):
        aes = AES256()
        data = b"Test data"
        encrypted_data = aes.encrypt(data)
        decrypted_data = aes.decrypt(encrypted_data)
        self.assertEqual(data, decrypted_data)

    def test_double_ratchet(self):
        ratchet = DoubleRatchet()
        data = b"Encrypted message"
        encrypted_data = ratchet.encrypt(data)
        decrypted_data = ratchet.decrypt(encrypted_data)
        self.assertEqual(data, decrypted_data)

if __name__ == '__main__':
    unittest.main()
