import os
import ssl
import socket

# Fetch TLS/SSL credentials from environment variables
HOST = os.getenv('UTRUST_HOST')
PORT = int(os.getenv('UTRUST_PORT'))
CLIENT_CERT = os.getenv('UTRUST_CLIENT_CERT')
CLIENT_KEY = os.getenv('UTRUST_CLIENT_KEY')
CA_CERT = os.getenv('UTRUST_CA_CERT')

# Create a TLS-secured socket
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.load_cert_chain(certfile=CLIENT_CERT, keyfile=CLIENT_KEY)
context.load_verify_locations(cafile=CA_CERT)
sock = context.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM), server_hostname=HOST)

# Connect to the device
sock.connect((HOST, PORT))

# Send and receive data securely
sock.send(b'Hello, uTrust 3700 F!')
response = sock.recv(1024)
print(f'Received response: {response.decode()}')

# Close the connection
sock.close()

