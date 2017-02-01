#!/usr/bin/env python
import smbus
import time
import datetime
import curses
import MySQLdb

import Adafruit_DHT
Adasensor = Adafruit_DHT.DHT11
pin = 26
humidity, temperature = Adafruit_DHT.read(Adasensor, pin)
if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to get reading. Try again!')




# 2014-08-26 PCF8591-x.py

# Connect Pi 3V3 - VCC, Ground - Ground, SDA - SDA, SCL - SCL.

# ./PCF8591-x.py


bus = smbus.SMBus(1)

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()

aout = 0

stdscr.addstr(5, 20, "BioBox Sensor Reading:")
stdscr.addstr(6, 20, "____________________")

stdscr.addstr(10, 0, "Temp")
stdscr.addstr(12, 0, "Light")
stdscr.addstr(14, 0, "Moist")
# stdscr.addstr(16, 0, "Resistor")

stdscr.nodelay(1)


try:

   while True:

      #for a in range(0,3):
      #   aout = aout + 1
      #   bus.write_byte_data(0x48,0x40 | ((a+1) & 0x03), aout)
      #   v = bus.read_byte(0x48)
      #   hashes = v / 4
      #   spaces = 64 - hashes
      #   stdscr.addstr(10+a*2, 12, str(v) + ' ')
      #   stdscr.addstr(10+a*2, 16, '#' * hashes + ' ' * spaces )
         
      #temp (AIN1)
      aout = aout + 1
      bus.write_byte_data(0x48,0x40 | ((2) & 0x03), aout)
      tempRead = bus.read_byte(0x48)
      hashes = tempRead / 4
      spaces = 64 - hashes
      stdscr.addstr(10, 12, str(tempRead) + ' ')
      stdscr.addstr(10, 16, '#' * hashes + ' ' * spaces )
      #light (AIN2)
      aout = aout + 1
      bus.write_byte_data(0x48,0x40 | ((3) & 0x03), aout)
      lightRead = bus.read_byte(0x48)
      hashes = lightRead / 4
      spaces = 64 - hashes
      stdscr.addstr(12, 12, str(lightRead) + ' ')
      stdscr.addstr(12, 16, '#' * hashes + ' ' * spaces )
      #moisture (AIN3)
      aout = aout + 1
      bus.write_byte_data(0x48,0x40 | ((4) & 0x03), aout)
      moistRead = bus.read_byte(0x48)
      hashes = moistRead / 4
      spaces = 64 - hashes
      stdscr.addstr(14, 12, str(moistRead) + ' ')
      stdscr.addstr(14, 16, '#' * hashes + ' ' * spaces )

      
      datetime = (time.strftime("%Y-%m-%d ") + time.strftime("%H:%M:%S"))

      #Server Connection to MySQL:
      conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="raspberry",
                  db="sensor_database")
      x = conn.cursor()
      try:
         x.execute("""INSERT INTO plant_log VALUES (%s,%s,%s,%s)""",(datetime,tempRead,lightRead,moistRead))
         conn.commit()
      except:
         conn.rollback()
      conn.close()   
      #End servier connection

      
      stdscr.refresh()
      time.sleep(.5)

      c = stdscr.getch()

      if c != curses.ERR:
         break

except:
   pass

curses.nocbreak()
curses.echo()
curses.endwin()
