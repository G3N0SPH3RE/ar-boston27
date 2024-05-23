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
#   DMR-280X-1120
#   Barcode Reader DataMan 280X
#   High Speed Reader

##########################################################
# Imports and important things
ip = '11.200.0.138'


############## End of Imports and things #############

# :::::: method B1 ::::::

#  RS-232 Communication with COGNEX BCR
#  replace '#' with com number
#  cognex = serial.Serial('COM#', 9600, timeout=5)
#  time.sleep(.5)
#  cognex.write(b'0') 
#  time.sleep(1) 
#  response = cognex.readline() 
#  cognexsn = response 
#  print(cognexsn) 
# cognexsn = cognexsn.decode() 
# print(cognexsn) 
# cognexsn = cognexsn.replace('\n', ' ').replace('\r', '').replace(' ','') 
# print(cognexsn)

####################### Method B1 END#############################

## :::::: method B2 ::::::

# from pylibhardware import proxy_simple
# # Cognex hardware ID

# vendor, product_name, zz = proxy_simple( '11.200.0.138' ).read( [('@1/1/1','INT'),('@1/1/7','SSTRING'),('@0x79/1/0x10','SINT')] )

# print(vendor)
# print(product_name)
# print(zz)

# if vendor == 'Cognex':
#     print('Vendor Match')
# else: print('Vendor does not match')

# if product_name == 'DMR-280X-1120': #Check this for accuracy...
#     print('Product Match')
# else: print('Product does not match')

# if zz == 'Barcode Reader DataMan 280X':
#     print('Barcode Reader DataMan 280X')
#     print('Barcode scanner is working')
# else:
#     print('Barcode Reader DataMan 280X')
#     print('Barcode scanner is not working')
            
####################### Method B2 END#############################

# :::::: method B3 ::::::

#  Ping IP address
import subprocess
import platform

ip_address = "11.200.0.138"

def ping_ip(host):
    """
    Pings the given IP address and returns True if the host responds, False otherwise.
    """
    # Determine the ping command based on the operating system
    param = '-n' if platform.system().lower() == 'windows' else '-c' #send single ping packet for windows(-n) and linux(-c)

    # Build the ping command
    command = ['ping', param, '1', host]

    try:
        # Run the ping command and check the return code
        return subprocess.call(command) == 0
    except:
        # If there's an error, return False
        return False

# Ping the IP address and log the result
if ping_ip(ip_address):
    print(f"Communication with {ip_address} is valid. Logging pass.")
else:
    print(f"Communication with {ip_address} failed. Logging fail.")

####################### Method B3 END#############################
