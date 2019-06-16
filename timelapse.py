from time import sleep
from glob import glob
from subprocess import check_output, CalledProcessError
import datetime
import numpy as np
#import cv2
#import picamera
import os
import sys

platform = sys.platform
#print(platform)

flashDriveName = 'SUPERMAN'

waitTime = 10

#give us some space to separate now from earlier
print("\n\n\n\n\n")

#SEARCH FOR FLASH DRIVES
#------------------------------------------------------
def get_usb_devices():
    sdb_devices = map(os.path.realpath, glob('/sys/block/sd*'))
    usb_devices = (dev for dev in sdb_devices
        if 'usb' in dev.split('/')[5])
    return dict((os.path.basename(dev), dev) for dev in usb_devices)
#------------------------------------------------------

#CREATE FOLDER METHOD
#------------------------------------------------------
def createFolder(directory):
	try:
		if not os.path.exists(directory):
			os.makedirs(directory)
			print('creating directory :' + directory)
		else:
			print(directory + ' folder already exists!')
	except OSError:
		print('Error: Creating directory. ' + directory)
#------------------------------------------------------

#check for flash drive (prefered) 
#ensure the 'lapses' folder exists
#                           #xxxxxxxxxxxxxxxxxxxxxxxxxxxxx     Delete when we
if (get_usb_devices() == {} || flashDriveName is None):# x <-- figure out the 
#   #no flash drive         #xxxxxxxxxxxxxxxxxxxxxxxxxxxxx     nameless USB issue
	print('No flash drive detected')
	newDirName = './lapses'
else:
	#there is flash drive 
	print('flash drive detected')
	if (flashDriveName not None):
		newDirName = "/Volumes/" + flashDriveName + "/lapses/"
	else:
		print('HOWEVER, I don\'t know how to use that memory address')
		print(get_usb_devices)
		newDirName = './lapses'
		#We know there is a flashdrive, just not the name, only
		#memory address... we'll work on that later..
#correctPath/lapses exists as newDirName
createFolder(newDirName)

now = datetime.datetime.now()
newDirName = newDirName + now.strftime("%m-%d-%Y_%H:%M")
#Directory name === ./lapses/MM_DD_YYYY-HH:MM
#create timelapse folder for this project
createFolder(newDirName) # <<-- THIS project's folder


#Loop for Linux

if (platform == 'linux'):
	import picamera
	with picamera.PiCamera() as camera:
		camera.resolution = (1024, 768)
		for filename in camera.capture_continuous(newDirName+'/img{timestamp:%H-%M-%S-%f}.jpg'):
			print("Image Captured:")
			sleep(waitTime)

if (platform == 'darwin'):
	print('Think Differently')
	'''cap = cv2.VideoCapture(0)
	while(True):
		ret, frame = cap.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.imshow('frame', frame)
		cv2.imshow('gray', gray)
		if cv2.waitKey(20) & 0xFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()'''