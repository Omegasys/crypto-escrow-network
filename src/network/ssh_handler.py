import paramiko
from src.crypto.chaCha20_poly1305 import ChaCha20Poly1305

class SSHHandler:
    def __init__(self, ssh_client):
        self.ssh_client = ssh_client
        self.chacha20 = ChaCha20Poly1305()

    def run_command(self, command):
        """Executes a command over SSH and encrypts the output."""
        stdin, stdout, stderr = self.ssh_client.exec_command(command)
        output = stdout.read()
        encrypted_output = self.chacha20.encrypt(output)
        print(f"Encrypted command output: {encrypted_output}")
        return encrypted_output

    def close_connection(self):
        """Closes the SSH connection."""
        self.ssh_client.close()
        print("SSH connection closed.")
