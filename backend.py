from sql import lastEntry;
from power import lightsOff,lightsOn;

temp = lastEntry("sensor_database","plant_log","Temp");
if (temp > 15):
    lightsOff();
else:
    lightsOn();
