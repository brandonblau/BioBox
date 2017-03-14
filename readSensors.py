#!/usr/bin/env python
import smbus
import time
import datetime
import MySQLdb
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
aout = 0;


try:

   for j in range(0,1):
         
      #temp & humidity
      aout = aout + 1
      bus.write_byte_data(0x48,0x40 | ((2) & 0x03), aout)
      tempRead = bus.read_byte(0x48)
      humidity, tempRead = Adafruit_DHT.read(Adasensor, pin)  
      if humidity is None and tempRead is None:
         try:
            x.execute("SELECT * FROM plant_log ORDER BY DateTime DESC LIMIT 1;");
            conn.commit();
            row = x.fetchone();
            tempRead = row[1];
            humidity = row[4];
         except:
            conn.rollback();
      else:
         tempRead = tempRead*9/5 + 32;
      
      #light
      aout = aout + 1
      bus.write_byte_data(0x48,0x40 | ((3) & 0x03), aout)
      lightRead = bus.read_byte(0x48)
      
      #soil moisture
      aout = aout + 1
      bus.write_byte_data(0x48,0x40 | ((4) & 0x03), aout)
      moistRead = bus.read_byte(0x48)

      #Server Connection to MySQL:
      conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="raspberry",
                  db="sensor_database")
      x = conn.cursor()
      datetime = (time.strftime("%Y-%m-%d ") + time.strftime("%H:%M:%S"))
      watered = 0
      try:
         if humidity is not None and tempRead is not None:
            lastTemp = tempRead
            x.execute("""INSERT INTO plant_log VALUES (%s,%s,%s,%s,%s,%s)""",(datetime,int(tempRead),lightRead,moistRead,humidity,watered))
            conn.commit()
         else:
            x.execute("""INSERT INTO plant_log VALUES (%s,%s,%s,%s,%s,%s)""",(datetime,int(lastTemp),lightRead,moistRead,humidity,watered))
            conn.commit()
      except:
         conn.rollback()

      #print('Time:'+str(datetime)+' Temp:'+str(tempRead)+' Light:'+str(lightRead)+' Moist:'+str(moistRead)+' Humidity:'+str(humidity));
      #time.sleep(10)

except:
   pass

conn.close(); 
