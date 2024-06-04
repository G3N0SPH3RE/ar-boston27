#### cognex camera/barcode capture test

###Imports, (not those kinds...)
import sys
import telnetlib
from ftplib import FTP
import time
import cv2

##############################

#### Cognex's config
def removeTagName(tag):
    return re.sub('<[^<]+?>', '', tag)


# host = "11.200.0.138" #DM280X
host = '11.200.0.154' #DM280-3.4

#DM260-A
# host = '11.200.0.191'
#DM260-B
# host = '11.200.0.192'
#DM260-C
# host = '11.200.0.193'
#DM260-D
# host = '11.200.0.194'

user = 'admin'
password = ''

### Method 1 ###

#### telnet login
tn = telnetlib.Telnet(host)
telnet_user = user+'\r\n'

tn.read_until('User: ') #wait for Camera prompts for username
tn.write(user + '\r\n') #send username
tn.read_until('Password: ') #wait for Camera prompts for password
tn.write(password + '\r\n') #send password

tn.read_until('Log In Confirmed') #wait for Camera to confirm login

#### capture
###Using 'Native Mode Command'; issues trigger=> camera must be set to manual
###network or external trigger mode
tn.write(b"SE8\r\n")

tn.read_until('1') #wait for Camera to respond, 1 = OK
tn.write('EV GetCellValue("B62")\r\n') #command to read the value on cell B62

qrCodeReturn = tn.read_until('</String>').split('\r\n') #print as XML tag

if qrCodeReturn[1] == '1':
    print('Good Read...')
    print('QR Code: ', removeTagName(qrCodeReturn[-1]))

##### Method 2 #####
# tn.write(telnet_user.encode('ascii')) #user name is admin
# tn.write("\r\n".encode('ascii')) #assuming no password - just return - now logged in
#print('Telnet Logged in')

# print('Image Captured')

### ftp login
# ftp = FTP(host)
# ftp.login(user)
#print('FTP logged in')

### show all file in cognex
# files_list = ftp.dir()
# print(files_list)

### download file from cognex
# filename = 'image.bmp'
# lf = open(filename, "wb")
# ftp.retrbinary("RETR " + filename, lf.write)
# lf.close()

# image = cv2.imread('image.bmp')
# cv2.imshow('Image', image)

# cv2.waitKey(0)
