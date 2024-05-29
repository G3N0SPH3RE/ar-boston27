#### cognex camera/barcode capture test

##############################

import sys
import telnetlib
from ftplib import FTP
import time
import cv2

# cognex's config
# ip = "11.200.0.138" #DM280X

#DM260-A
ip = '11.200.0.191'
#DM260-B
# ip = '11.200.0.192'
#DM260-C
# ip = '11.200.0.193'
#DM260-D
# ip = '11.200.0.194'

user = 'admin'
password = ''

# telnet login
tn = telnetlib.Telnet(ip)
telnet_user = user+'\r\n'
tn.write(telnet_user.encode('ascii')) #user name is admin
tn.write("\r\n".encode('ascii')) #assuming no password - just return - now logged in
#print('Telnet Logged in')

# capture
tn.write(b"SE8\r\n")

# ftp login
ftp = FTP(ip)
ftp.login(user)
#print('FTP logged in')

# show all file in cognex
# files_list = ftp.dir()
# print(files_list)

# download file from cognex
filename = 'image.bmp'
lf = open(filename, "wb")
ftp.retrbinary("RETR " + filename, lf.write)
lf.close()

image = cv2.imread('image.bmp')
cv2.imshow('Image', image)

cv2.waitKey(0)
