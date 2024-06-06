
############ v1 - BASIC PORT TEST ###############
import socket
import time

# Device IP address and port number
ip_address = "11.200.0.193"
port = 23  # Replace with the actual port number

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the device
    sock.connect((ip_address, port))
    print(f"Connected to {ip_address}:{port}")

    # Maintain the connection
    while True:
        # Send a keep-alive message or perform any necessary operations
        sock.sendall(b"keep-alive")
        
        # Wait for a short period before sending the next keep-alive
        time.sleep(10)  # Adjust the delay as needed

except socket.error as e:
    print(f"Error connecting to {ip_address}:{port}: {e}")

finally:
    # Close the socket connection
    sock.close()
    print(f"Connection to {ip_address}:{port} closed.")

# #################### v2 #######################
# import socket
# import time

# # Device IP address and port number
# ip_address = "11.200.0.193"
# port = 23  # Replace with the actual port number

# # Create a socket object
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# try:
#     # Connect to the device
#     sock.connect((ip_address, port))
#     print(f"Connected to {ip_address}:{port}")

#     # Send commands to the device
#     while True:
#         # Prompt the user for a command to send
#         command = input("Enter a command to send (or 'exit' to quit): ")
#         print(f"Sending command: {command}")
#         sock.sendall(command.encode())

#         if command.lower() == "exit":
#             break

#         # Send the command to the device
#         sock.sendall(command.encode())

#         # Wait for a response, with a timeout
#         start_time = time.time()
#         timeout = 5  # Adjust the timeout value as needed
#         response = b""
#         while time.time() - start_time < timeout:
#             try:
#                 data = sock.recv(1024)
#                 if not data:
#                     break
#                 response += data
#             except socket.timeout:
#                 print("Timeout waiting for response. Retrying...")
#                 sock.sendall(command.encode())
#                 continue

#         if not response:
#             print("No response received from the device.")
#         else:
#             print(f"Response: {response.decode()}")

# except socket.error as e:
#     print(f"Error connecting to {ip_address}:{port}: {e}")

# finally:
#     # Close the socket connection
#     sock.close()
#     print(f"Connection to {ip_address}:{port} closed.")
