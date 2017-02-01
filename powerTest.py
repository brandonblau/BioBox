import time
import RPi.GPIO as GPIO

#while True:
#    GPIO.setmode(GPIO.BCM)
#    GPIO.setup(12, GPIO.OUT)
#    print('HIGH BRUH!')
#    GPIO.output(12, GPIO.HIGH)
#    time.sleep(6)
#    GPIO.output(12, GPIO.LOW)
#    print('LOW!')
#    time.sleep(6)


GPIO.setmode(GPIO.BCM);
GPIO.setup(12, GPIO.OUT);
GPIO.setwarnings(False);

if GPIO.input(12):   #(returns 1 if on)
    GPIO.output(12, GPIO.LOW)
else:
    GPIO.output(12, GPIO.HIGH);
    
