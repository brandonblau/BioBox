import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

try:
   while 1:
       print GPIO.input(4)
       sleep(1)

except Keyboardinterrupt:
   GPIO.cleanup()


