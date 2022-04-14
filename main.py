import firebase_admin
from firebase_admin import db

import RPi.GPIO as GPIO
from time import sleep

in1 = 24
in2 = 23
en = 25
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p=GPIO.PWM(en,1000)


cred_obj = firebase_admin.credentials.Certificate('trash-114b6-firebase-adminsdk-8badn-af95caff8a.json')
default_app = firebase_admin.initialize_app(cred_obj, {'databaseURL': 'https://trash-114b6-default-rtdb.firebaseio.com/'})
p.start(25)

while True:
	status = db.reference("/data/status").get()
	speed = db.reference("/data/speed").get()
	if status == True:
		GPIO.output(in1,GPIO.HIGH)
		GPIO.output(in2,GPIO.LOW)
		p.ChangeDutyCycle(speed)
	if status == False:
		GPIO.output(in1,GPIO.LOW)
		GPIO.output(in2,GPIO.LOW)
