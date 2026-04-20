import unittest
from network.tunnel import create_secure_tunnel
from network.tcp_handler import TCPHandler
from network.ssh_handler import SSHHandler
from utils.network_utils import create_tcp_connection, send_data_over_tcp, receive_data_over_tcp

class TestNetwork(unittest.TestCase):

    def test_secure_tunnel(self):
        tunnel = create_secure_tunnel('localhost', 8080)
        self.assertTrue(tunnel.is_open())

    def test_tcp_connection(self):
        host = 'localhost'
        port = 8080
        sock = create_tcp_connection(host, port)
        self.assertIsNotNone(sock)
        sock.close()

    def test_send_receive_data(self):
        sock = create_tcp_connection('localhost', 8080)
        data = b"Test message"
        send_data_over_tcp(sock, data)
        received_data = receive_data_over_tcp(sock)
        self.assertEqual(data, received_data)

    def test_tcp_handler(self):
        handler = TCPHandler()
        self.assertIsInstance(handler, TCPHandler)

    def test_ssh_handler(self):
        handler = SSHHandler()
        self.assertIsInstance(handler, SSHHandler)

if __name__ == '__main__':
    unittest.main()
