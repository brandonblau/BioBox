import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False);
GPIO.setmode(GPIO.BCM);
GPIO.setup(4, GPIO.OUT);

def togglePump():

    if GPIO.input(4):   #(returns 1 if on)
        GPIO.output(4, GPIO.LOW);
        print('Pump switched on');
    else:
        GPIO.output(4, GPIO.HIGH);
        print('Pump switched off');

def pumpOn():
    GPIO.output(4, GPIO.LOW);
    print('Pump switched on');

def pumpOff():
    GPIO.output(4, GPIO.HIGH);
    print('Pump switched off');
    

