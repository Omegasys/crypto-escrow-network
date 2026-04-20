import unittest
from utils.encryption_utils import encrypt_data_aes, decrypt_data_aes, generate_rsa_keys
from utils.time_utils import apply_random_delay
from utils.network_utils import create_tcp_connection, send_data_over_tcp, receive_data_over_tcp
from utils.logging import log_info, log_error, setup_logging

class TestUtils(unittest.TestCase):

    # Test Encryption Helpers
    def test_aes_encryption(self):
        data = "Sensitive information"
        key = b'Sixteen byte key'
        encrypted_data = encrypt_data_aes(data, key)
        decrypted_data = decrypt_data_aes(encrypted_data, key)
        self.assertEqual(data, decrypted_data)

    def test_rsa_key_generation(self):
        private_key, public_key = generate_rsa_keys()
        self.assertIsNotNone(private_key)
        self.assertIsNotNone(public_key)

    # Test Time Utils
    def test_apply_random_delay(self):
        # This is a simple test; you might want to mock the `time.sleep` to avoid actual delays in unit tests.
        try:
            apply_random_delay(1, 2)  # This should apply a random delay between 1 and 2 seconds.
            self.assertTrue(True)  # If it doesn't raise an error, the test passes.
        except Exception as e:
            self.fail(f"apply_random_delay raised an exception: {e}")

    # Test Network Utils
    def test_tcp_connection(self):
        host = 'localhost'
        port = 8080
        try:
            sock = create_tcp_connection(host, port)
            self.assertIsNotNone(sock)
            sock.close()
        except Exception as e:
            self.fail(f"create_tcp_connection raised an exception: {e}")

    def test_send_receive_data(self):
        host = 'localhost'
        port = 8080
        data = b"Test data"
        try:
            sock = create_tcp_connection(host, port)
            send_data_over_tcp(sock, data)
            received_data = receive_data_over_tcp(sock)
            self.assertEqual(data, received_data)
        except Exception as e:
            self.fail(f"TCP communication raised an exception: {e}")

    # Test Logging
    def test_logging(self):
        setup_logging()
        try:
            log_info("Test info message")
            log_error("Test error message")
            self.assertTrue(True)  # If no exceptions were raised, the test passes.
        except Exception as e:
            self.fail(f"Logging raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()
