import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setwarnings(False)

while(True):
	GPIO.output(10,True)
  	GPIO.output(16,True)
	GPIO.output(18,True)
	print("\nLEDs are ON")
	time.sleep(1)
	GPIO.output(10,False)
	GPIO.output(16,False)
	GPIO.output(18,False)
	print("\nLEDs are OFF")
	time.sleep(1)
	
GPIO.cleanup()
