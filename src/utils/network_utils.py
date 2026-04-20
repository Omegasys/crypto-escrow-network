import socket

def create_tcp_connection(host, port):
    """Creates a TCP connection to the specified host and port."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    return sock

def send_data_over_tcp(sock, data):
    """Sends encrypted data over a TCP connection."""
    sock.sendall(data)
    print(f"Sent data: {data}")

def receive_data_over_tcp(sock):
    """Receives data over a TCP connection."""
    data = sock.recv(1024)
    print(f"Received data: {data}")
    return data
