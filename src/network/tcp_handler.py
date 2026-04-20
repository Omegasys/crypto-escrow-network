import socket
from src.crypto.chaCha20_poly1305 import ChaCha20Poly1305

class TCPHandler:
    def __init__(self, tcp_socket):
        self.tcp_socket = tcp_socket
        self.chacha20 = ChaCha20Poly1305()

    def send_data(self, data):
        """Encrypts and sends data over the TCP connection."""
        encrypted_data = self.chacha20.encrypt(data)
        self.tcp_socket.sendall(encrypted_data)
        print(f"Sent encrypted data: {encrypted_data}")

    def receive_data(self):
        """Receives encrypted data and decrypts it."""
        encrypted_data = self.tcp_socket.recv(1024)
        decrypted_data = self.chacha20.decrypt(encrypted_data)
        print(f"Received decrypted data: {decrypted_data}")
        return decrypted_data
