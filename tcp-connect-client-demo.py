
############ TCP Connection ##############

import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set the host and port
host = "11.200.0.0"
port = 31415

# Bind the socket to the host and port
sock.bind((host, port))

# Listen for incoming connections
sock.listen(1)

print(f"Server is listening on {host}:{port}")

while True:
    print("Waiting for a connection...")
    connection, client_address = sock.accept()
    try:
        print(f"Connection from {client_address}")

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print(f"Received: {data.decode()}")
            if data:
                print(f"Sending data back to the client")
                connection.sendall(data)
            else:
                print("No more data from", client_address)
                break

    finally:
        # Clean up the connection
        connection.close()



# ############### TCP client ###############
# import socket

# # Create a TCP/IP socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Connect the socket to the server
# server_address = ("11.200.0.0", 31415)
# print(f"Connecting to {server_address}")
# sock.connect(server_address)

# try:
#     # Send data
#     message = b"This is the message. It will be repeated."
#     print(f"Sending {message}")
#     sock.sendall(message)

#     # Look for the response
#     amount_received = 0
#     amount_expected = len(message)
#     while amount_received < amount_expected:
#         data = sock.recv(16)
#         amount_received += len(data)
#         print(f"Received: {data.decode()}")

# finally:
#     print("Closing socket")
#     sock.close()
