#!/usr/bin/env python
import smbus
import time
import datetime
import MySQLdb

#ADAFRUIT:
import Adafruit_DHT
Adasensor = Adafruit_DHT.DHT11
pin = 26
lastTemp = 0;

# 2014-08-26 PCF8591-x.py

# Connect Pi 3V3 - VCC, Ground - Ground, SDA - SDA, SCL - SCL.

# ./PCF8591-x.py

#Server Connection to MySQL:
conn = MySQLdb.connect(host= "localhost",
    user="root",
    passwd="raspberry",
    db="sensor_database")
x = conn.cursor()

bus = smbus.SMBus(1)
aout = 0
try:

   while True:
       
      datetime = (time.strftime("%Y-%m-%d ") + time.strftime("%H:%M:%S"))
      
      #for a in range(0,3):
      #   aout = aout + 1
      #   bus.write_byte_data(0x48,0x40 | ((a+1) & 0x03), aout)
      #   v = bus.read_byte(0x48)
      #   hashes = v / 4
      #   spaces = 64 - hashes
      #   stdscr.addstr(10+a*2, 12, str(v) + ' ')
      #   stdscr.addstr(10+a*2, 16, '#' * hashes + ' ' * spaces )
         

      #aout = aout + 1
      #light (AIN2)
      aout = aout + 1
      bus.write_byte_data(0x48,0x40 | ((3) & 0x03), aout)
      lightRead = bus.read_byte(0x48)
      #moisture (AIN3)
      aout = aout + 1
      bus.write_byte_data(0x48,0x40 | ((4) & 0x03), aout)
      moistRead = bus.read_byte(0x48)    
      #temp (AIN1)
          #bus.write_byte_data(0x48,0x40 | ((2) & 0x03), aout)
          #tempRead = bus.read_byte(0x48)
      humidity, tempRead = Adafruit_DHT.read(Adasensor, pin)
      if humidity is not None and tempRead is not None:
          lastTemp = tempRead
          try:
              x.execute("""INSERT INTO plant_log VALUES (%s,%s,%s,%s)""",(datetime,int(tempRead),lightRead,moistRead))
              conn.commit()
          except:
              conn.rollback()
      else:
          try:
              x.execute("""INSERT INTO plant_log VALUES (%s,%s,%s,%s)""",(datetime,int(lastTemp),lightRead,moistRead))
              conn.commit()
          except:
              conn.rollback()
    
      #Server Connection to MySQL:
      #conn = MySQLdb.connect(host= "localhost",
      #            user="root",
      #            passwd="raspberry",
      #            db="sensor_database")
      #x = conn.cursor()
      
   
      #End servier connection
      #conn.close()
      time.sleep(.5)

except:
   pass

conn.close()
