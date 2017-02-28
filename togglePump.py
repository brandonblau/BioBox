import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False);
GPIO.setmode(GPIO.BCM);
GPIO.setup(6, GPIO.OUT);

def togglePump():

    if GPIO.input(6):   #(returns 1 if on)
        GPIO.output(6, GPIO.LOW)
        print('Power switched off');
    else:
        GPIO.output(6, GPIO.HIGH);
        print('Power switched on');


togglePump();

