import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False);
GPIO.setmode(GPIO.BCM);
GPIO.setup(12, GPIO.OUT);

if GPIO.input(12):   #(returns 1 if on)
    GPIO.output(12, GPIO.LOW)
    print('Power switched off');
else:
    GPIO.output(12, GPIO.HIGH);
    print('Power switched on');

