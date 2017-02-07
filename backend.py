from lastEntry import lastEntry;
from powerToggle import lightsOff,lightsOn;

temp = lastEntry("sensor_database","plant_log","Temp");
if (temp > 60):
    lightsOff();
else:
    lightsOn();
#lightsOn();
