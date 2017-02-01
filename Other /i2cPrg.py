import time

from smbus import SMBus

bus = SMBus(1)

bus.write_byte(0x48, 0) #i2cget -y 1
last_reading = -1

while (0 == 0): #do forever
        reading = bus.read_byte(0x48) #read A/D
        print('analog reading: '+str(reading))
        time.sleep(3) #slep 3 seconds)
        
