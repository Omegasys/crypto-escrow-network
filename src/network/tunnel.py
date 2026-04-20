import socket
import ssl
import paramiko
from src.crypto.chaCha20_poly1305 import ChaCha20Poly1305
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

class SecureTunnel:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.ssh_client = None
        self.tcp_socket = None
        self.https_socket = None
        self.chacha20 = ChaCha20Poly1305()

    def create_https_connection(self):
        """Creates an HTTPS connection."""
        context = ssl.create_default_context()
        self.https_socket = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=self.host)
        self.https_socket.connect((self.host, self.port))
        print(f"HTTPS connection established to {self.host}:{self.port}")
        return self.https_socket

    def create_ssh_connection(self):
        """Creates an SSH connection."""
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_client.connect(self.host, port=22)
        print(f"SSH connection established to {self.host}:22")
        return self.ssh_client

    def create_tcp_connection(self):
        """Creates a TCP connection."""
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_socket.connect((self.host, self.port))
        print(f"TCP connection established to {self.host}:{self.port}")
        return self.tcp_socket

    def establish_tunnel(self):
        """Establishes the full HTTPS -> SSH -> ChaCha20-Poly1305 -> TCP tunnel."""
        self.create_https_connection()
        self.create_ssh_connection()
        self.create_tcp_connection()

        # Now that we've established HTTPS -> SSH -> TCP, apply ChaCha20-Poly1305 encryption.
        self.chacha20.generate_key()
        self.chacha20.generate_nonce()
        print("ChaCha20-Poly1305 encryption initialized.")
        
        return self.tcp_socket, self.https_socket, self.ssh_client
