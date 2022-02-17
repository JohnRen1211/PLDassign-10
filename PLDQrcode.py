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
