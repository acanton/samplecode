# Input Polling 
# Python code checks the current value of a GPIO input pin at a regular interval.
# When the GPIO changes value, this means that the button has been pressed.



import RPI.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(18, GPIO.LOW)

try:
	while True:
		if (GPIO.input(24) == GPIO.LOW):
			print ('Back Door')
			GPIO.output(18, GPIO.HIGH)
		elif (GPIO.input(25) == GPIO.LOW):
			print ('Front Door')
			GPIO.output(18, GPIO.HIGH)
		else:
			GPIO.output(18, GPIO.LOW)
		time.sleep(0.1)
except KeyboardInterrupt:
	GPIO.cleanup()
print('End of Test')
