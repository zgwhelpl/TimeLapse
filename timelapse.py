from time import sleep
import datetime
import picamera
import os
import sys

waitTime = 10

def createFolder(directory):
	try:
		if not os.path.exists(directory):
			os.makedirs(directory)
		else:
			print(directory + ' folder already exists!')
	except OSError:
		print('Error: Creating directory. ' + directory)

#ensure the 'lapses' folder exists
createFolder('./lapses')

#Directory name === MM_DD_YYYY-HH:MM
now = datetime.datetime.now()
newDirName = now.strftime("%m-%d-%Y_%H:%M")

#Directory name === ./lapses/MM_DD_YYYY-HH:MM
print "Making directory " + newDirName
newDirName = './lapses/' + newDirName

#create timelapse folder for this project
createFolder(newDirName)

#Loop
with picamera.PiCamera() as camera:
	camera.resolution = (1024, 768)
	for filename in camera.capture_continuous(newDirName+'/img{timestamp:%H-%M-%S-%f}.jpg'):
		print("Image Captured:")
		sleep(waitTime)