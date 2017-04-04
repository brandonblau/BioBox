#!/usr/bin/env python
import smbus;
import time;
import datetime;
import MySQLdb;
import Adafruit_DHT;
import RPi.GPIO as GPIO
from sql import avgDailyValue
import smtplib
import time
import email
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

settingsFile = open("/home/pi/Desktop/settings.txt");

for line in settingsFile:
    if (line.find(

dhtPin = 26;
pumpPin = 4;
lightPin = 12;
fromaddr = "bioboxdev@gmail.com"
toaddr = "brandonblau@me.com"

GPIO.setwarnings(False);
GPIO.setmode(GPIO.BCM);
GPIO.setup(pumpPin, GPIO.OUT);
GPIO.setup(lightPin, GPIO.OUT);

def dailyUpdate():
         
    msg = MIMEMultipart()
         
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Biobox daily update"+time.strftime(" %Y-%m-%d ")
         
    line1 = '  Biobox dailyupdate ' + time.strftime(" %Y-%m-%d ")
    line2 = '------------------------------------'
    line3 = 'Average temp: ' + str(avgDailyValue("Temp"))
    line4 = 'Average light: ' + str(avgDailyValue("Light"))
    line5 = 'Average moisture: ' + str(avgDailyValue("Moist"))
    line6 = 'Average humidity: ' + str(avgDailyValue("Humidity"))
    line7 = 'Average watered: ' + str(avgDailyValue("Watered"))
    body = line1 + '/r' + line2 + '/r' + line3 + line4 + '/r'  + line5 + '/r'  + line6 + '/r'  + line7

    msg.attach(MIMEText(body, 'plain'))
         
    filename = "cam.jpg"
         
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "tinyrick")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


def lightsOff():
    GPIO.output(lightPin, GPIO.LOW);

def lightsOn():
    GPIO.output(lightPin, GPIO.HIGH);

def pumpOn():
    GPIO.output(pumpPin, GPIO.LOW);

def pumpOff():
    GPIO.output(pumpPin, GPIO.HIGH);

def readSensors():
    dht = Adafruit_DHT.DHT11;

    #Server Connection to MySQL:
    conn = MySQLdb.connect(host= "localhost",user="root",passwd="raspberry",db="sensor_database");
    x = conn.cursor();

    bus = smbus.SMBus(1);
    aout = 0;
    try:
        for j in range(0,1):
            #temp & humidity
            aout += 1
            bus.write_byte_data(0x48,0x40 | ((2) & 0x03), aout)
            temp = bus.read_byte(0x48);
            humidity, temp = Adafruit_DHT.read(dht, dhtPin);

            if humidity is None and temp is None:
                try:
                    x.execute("SELECT * FROM plant_log ORDER BY DateTime DESC LIMIT 1;");
                    conn.commit();
                    row = x.fetchone();
                    temp = row[1];
                    humidity = row[4];
                except:
                    conn.rollback();
            else:
                temp = temp*9/5 + 32;

            #light
            aout += 1
            bus.write_byte_data(0x48,0x40 | ((3) & 0x03), aout)
            light = bus.read_byte(0x48)

            #soil moisture
            aout += 1
            bus.write_byte_data(0x48,0x40 | ((4) & 0x03), aout)
            moisture = bus.read_byte(0x48)

            datetime = (time.strftime("%Y-%m-%d ") + time.strftime("%H:%M:%S"))
            watered = 0;
            
            try:
                if humidity is not None and temp is not None:
                    x.execute("""INSERT INTO plant_log VALUES (%s,%s,%s,%s,%s,%s)""",(datetime,int(temp),light,moisture,humidity,watered))
                    conn.commit();
                else:
                    x.execute("""INSERT INTO plant_log VALUES (%s,%s,%s,%s,%s,%s)""",(datetime,int(temp),light,moisture,humidity,watered))
                    conn.commit();
            except:
                conn.rollback();
    except:
        pass;
    conn.close(); 

