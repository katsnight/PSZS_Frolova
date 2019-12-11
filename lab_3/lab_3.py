import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
arr = [7,18,15,12]

while True:
	for i in arr:
                if i == 11:
                    		GPIO.cleanup()
		GPIO.setup(i, GPIO.OUT)
		GPIO.output(i, True)
		time.sleep(0.1)

	for i in arr:

		GPIO.setup(i, GPIO.OUT)
		GPIO.output(i, False)
		time.sleep(0.1)


