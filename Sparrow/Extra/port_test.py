import socket

# Device IP address and port number
ip_address = "11.200.0.54"
port = 23  # Replace with the required port number

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the device
    sock.connect((ip_address, port))
    print(f"Connected to {ip_address}:{port}")

    # Send and receive data as needed
    # ...

except socket.error as e:
    print(f"Error connecting to {ip_address}:{port}: {e}")

finally:
    # Close the socket connection
    sock.close()
