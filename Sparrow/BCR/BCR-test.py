#  Barcode scanner test

funame= """
.-. .-')                  _  .-')           .-') _     ('-.    .-')    .-') _    
\  ( OO )                ( \( -O )         (  OO) )  _(  OO)  ( OO ). (  OO) )   
 ;-----.\       .-----.   ,------.         /     '._(,------.(_)---\_)/     '._  
 | .-.  |      '  .--./   |   /`. '   .-') |'--...__)|  .---'/    _ | |'--...__) 
 | '-' /_)     |  |('-.   |  /  | | _(  OO)'--.  .--'|  |    \  :` `. '--.  .--' 
 | .-. `.     /_) |OO  )  |  |_.' |(,------.  |  |  (|  '--.  '..`''.)   |  |    
 | |  \  |    ||  |`-'|   |  .  '.' '------'  |  |   |  .--' .-._)   \   |  |    
 | '--'  /.-.(_'  '--'\.-.|  |\  \            |  |   |  `---.\       /   |  |    
 `------' `-'   `-----'`-'`--' '--'           `--'   `------' `-----'    `--'    
"""
print(funame)

##########################################################

#  Initial attempt: To call hardware id and check to see if it matches.
# If ID does not match, then send error to ????

#  Things to do:
#      Set scanner IP = 11.200.0.138 ; per Sparrow manual
#      Where is error log being sent?
#      Test scanner actualy functionality?

# Device Info:
#   Cognex
#   DMR-280X-1120 #CHECK THIS?
#   Barcode Reader DataMan 280X
#   High Speed Reader

# SOME COMMANDS
#  ACTIONS: SET / GET
 # LIVEIMG.MODE - controls live image display; 
    # ARGUMENT: mode; mode range= [0,2  ] 0:Disable and 2:Enable
# LIVEIMG.SEND - Request image transfer to PC when LIVEIMG.MODE is set to 3; 
    # ARGUMENT: size [0-3]; format [0-2] 0=BMP, 1:JPEG, 2:PNG; quality [10,15,20...85,90] : JPEG Quality

##########################################################
# Imports and important things

#DM280X
# ip = '11.200.0.138'

#DM260-A
# ip = '11.200.0.191'

#DM260-B
# ip = '11.200.0.192'

#DM260-C
ip = '11.200.0.193'

#DM260-D
# ip = '11.200.0.194'

port = 23


############## End of Imports and things #############

# :::::: method 1 ::::::
###This works####

# #  Ping IP address
# import subprocess
# import platform

# # DM280X ip = "11.200.0.138"

# def ping_ip(host):
#     """
#     Pings the given IP address and returns True if the host responds, False otherwise.
#     """
#     # Determine the ping command based on the operating system
#     param = '-n' if platform.system().lower() == 'windows' else '-c' #send single ping packet for windows(-n) and linux(-c)

#     # Build the ping command
#     command = ['ping', param, '1', host]

#     try:
#         # Run the ping command and check the return code
#         return subprocess.call(command) == 0
#     except:
#         # If there's an error, return False
#         return False

# # Ping the IP address and log the result
# if ping_ip(ip):
#     print(f"Communication with {ip} is valid. Logging pass.")
# else:
#     print(f"Communication with {ip} failed. Logging fail.")

####################### Method B1 END#############################

import telnetlib
import time

# Telnet connection details
# ip = "11.200.0.193"
# port = 23
# user = "admin"
# password = ""

print("Connecting to Cognex camera @ ", ip, " on port ", port)

# Telnet command
command = b"||>GET DEVICE.NAME\r\n"

try:
    # Connect to the Telnet server
    tn = telnetlib.Telnet(ip, port, timeout=5)

    # tn.read_until(b"User: ", timeout=5)    # Wait for the login prompt
    # tn.write(user.encode() + b"\r\n")            # Send the username
    # tn.read_until(b"Password: ", timeout=5)           # Wait for the password prompt
    # tn.write(password.encode() + b"\r\n")                 # Send the password
    # tn.read_until(b"Log In Confirmed", timeout=5)             # Wait for the login confirmation

    # Send the command
    tn.write(command)

    # Read the response
    response = tn.read_until(b"\n", timeout=5)
    print(response.decode().strip())

    while True:
        # Prompt the user for a command
        user_input = input("Enter a command (or 'exit' to quit): ")

        # Check if the user wants to exit
        if user_input.lower() == "exit":
            break

        # Add the '||>' prefix to the user input
        command = (b"||>" + user_input.encode() + b"\r\n")

        # Send the command
        tn.write(command)

        # Read the response
        response = tn.read_until(b"\n", timeout=5)
        print(response.decode().strip())

    # Close the connection
    tn.close()

except Exception as e:
    print(f"Error: {e}")
