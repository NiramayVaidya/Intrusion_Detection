'''
The program sends a push notification to the Pushbullet Chrome Extension configured by the computer's user
(ideally, instead of using the Pushbullet Chrome Extension, the Pushbullet mobile application should be used)
The push notification asks whether the person currently operating the computer is indeed the computer's user
If the user responds with a no to the push notification, then the intrusion detection control function kicks in
The control function displays an intruder suspected message
It then captures a real time picture of the person who is currently operating the computer and sends it via another push
notification to the user
It finally logs off from the computer i.e. shuts it down
On the other hand, if the user responds with a yes, then the program exits
'''

import cv2
import numpy as np
from pushbullet import PushBullet
import win32com.client as wincl
import time
import os

# Display the intruder suspected message
def suspected_message():
    speak = wincl.Dispatch('SAPI.SpVoice')
    speak.Speak('Intruder Suspected')

# Take the intruder's picture
def intruder_pic():
	cam=cv2.VideoCapture(0)
	s, im = cam.read()
	# cv2.imshow('Intruder Picture', im)
	cv2.imwrite("Intruder_Picture.png", im)

# Push the captured image to the Pushbullet Chrome Extension
def image_send():
	with open('Intruder_Picture.png', 'rb') as pic:
		file_data = pb.upload_file(pic, 'Intruder_Picture.png')
	push = pb.push_file(**file_data)

# Log off from the computer if intruder is suspected (shuts down the computer)
def log_off():
	os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')

# The intrusion detection control function
def control():
	while True:
		val = pb.get_pushes()
		try:
			action = val[0]['body']
		except KeyError:
			print('Could not identify body of the action')
		print(action)
		if action.lower() == 'no':
			suspected_message()
			intruder_pic()
			image_send()
			time.sleep(15)
			log_off()
		elif action.lower() == 'yes':
			break
		else:
			pass

if __name__ == '__main__':
	# User's PushBullet API key
	api_key = '<api_key>'
	pb = PushBullet(api_key)
	push_msg = pb.push_note("PYTHON : ", "Found Internet Connectivity, is this you? If not, message 'No' ")

	control()
