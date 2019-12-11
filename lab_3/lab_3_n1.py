import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
arr = [7,8,18,16,15,13,12,11]

while True:
	for i in arr:
		GPIO.setup(i, GPIO.OUT)
		GPIO.output(i, True)
		time.sleep(0.1)
	for i in arr:
		GPIO.setup(i, GPIO.OUT)
		GPIO.output(i, False)
		time.sleep(0.1)
