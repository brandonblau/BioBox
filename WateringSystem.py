from sql import lastEntry;
from emailBot import sendEmail
import time;
import MySQLdb
from pump import pumpOn,pumpOff;

moist = lastEntry("sensor_database","plant_log","Moist");

if (moist > 50):
    pumpOn();
    watered = 1;
    time.sleep(30);
    pumpOff();
else:
    pumpOff();
    watered = 0;

if watered == 1:
    #Server Connection to MySQL:
      conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="raspberry",
                  db="sensor_database")
      x = conn.cursor()
      try:
          x.execute("""UPDATE plant_log SET Watered=1 ORDER BY DateTime DESC LIMIT 1;""")
          conn.commit()
          sendEmail("The plant has been watered and the database has been updated")
      except:
         conn.rollback()


