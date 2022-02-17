# Program for Qrcode reader
# Notes:
# Make program taht will scan qr code
# Program should read qrcode using ebcam and save the information into text document
# The date and time when program run should be save into text file 


print('Qr Code reader open')

# Import libraries
import cv2
from pyzbar.pyzbar import decode
import datetime

# Create program for time checker
now = datetime.datetime.now()
data_time = (now.strftime('%y-%m-%d %H: %M:%S'))
print('Time the Qrcode reader is used:')
print (data_time)

# Code for camera
capture = cv2.VideoCapture(0)
recieved_data = None

# Condition code
while True:
    _,frame = capture.read()

    decoded_data = decode(frame)
    try:
        data=(decoded_data[0][0])
        if data != recieved_data:
            print(data)
            recieved_data = data
    except:
        pass

    cv2.imshow('QR Code Scanner', frame)

    key = cv2.waitKey(1)

    if key == 27:
        break

# Text file creator
with open('data.txt', 'w') as f:
    f.write(str(recieved_data))
    f.write('\n')

# Text file creator