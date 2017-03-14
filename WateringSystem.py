from sql import lastEntry;
import time;
from pump import pumpOn,pumpOff;

moist = lastEntry("sensor_database","plant_log","Moist");
if (moist > 50):
    pumpOn();
    time.sleep(30);
    pumpOff();
else:
    pumpOff();
