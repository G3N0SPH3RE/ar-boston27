# cognex-bcr-with-python

## pip install telnetlib3
## pip install pyftpdlib
## pip install opencv-python

#### get_image.py ####

This code is a Python script that interacts with a Cognex camera to capture and display an image. 
Let's go through the code step by step:

The script imports the necessary modules: sys, telnetlib, ftplib, time, and cv2 (OpenCV).

The script defines the Cognex camera's configuration, including the IP address, username, and password.

The script establishes a Telnet connection to the Cognex camera using the 
telnetlib.Telnet() function. It logs in using the provided username and an empty password.

The script sends the "SE8" command to the Cognex camera via the Telnet connection, which is likely a command to capture an image.

The script then establishes an FTP connection to the Cognex camera using the 
ftplib.FTP() function and logs in using the provided username.

The script downloads the captured image file (named "image.bmp") from the Cognex camera using the 
ftp.retrbinary() function and saves it to the local file system.

The script then uses the 
cv2.imread() function from the OpenCV library to load the downloaded image file and displays it using the 
cv2.imshow() function.

Finally, the script waits for the user to press a key (cv2.waitKey(0)) before exiting.

######################################################

#### stream.py ####

This code is a Python script that captures images from a Cognex camera and displays them using OpenCV. Let's go through the code step by step:

The script imports the necessary modules: sys, telnetlib, ftplib, time, and cv2 (OpenCV).

The script defines the Cognex camera's configuration, including the IP address, username, and password.

The script enters a while True loop, which will continuously capture and display images from the camera.

Inside the loop, the script:

    Starts a timer using time.time()

    Establishes a Telnet connection to the Cognex camera using 
    telnetlib.Telnet() and logs in using the provided username and an empty password.

    Sends the "SE8" command to the Cognex camera via the Telnet connection, which is likely a command to capture an image.

    Establishes an FTP connection to the Cognex camera using 
    ftplib.FTP() and logs in using the provided username.

    Downloads the captured image file (named "image.bmp") from the Cognex camera using the 
    ftp.retrbinary() function and saves it to the local file system with the name "image_get.bmp".

    Loads the downloaded image file using cv2.imread() and displays it using cv2.imshow().

Prints the time it took to capture and display the image.

The script then checks if the user has pressed the 'q' key using 
cv2.waitKey(1). If the key is pressed, the loop is broken.

Finally, the script closes all the OpenCV windows using cv2.destroyAllWindows().

#######################################