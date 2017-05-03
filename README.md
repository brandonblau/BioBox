# BioBox
![BioBox][https://github.com/brandonblau/BioBox/blob/master/Resources/BioBoxLogoSmall.jpg?raw=true]
LMU Senior Project 2017

## Things you will need
- $35 [Raspberry Pi 3](https://www.amazon.com/Raspberry-Pi-RASPBERRYPI3-MODB-1GB-Model-Motherboard/dp/B01CD5VC92)
- $9.99 [Raspberry Pi Power Supply](https://www.amazon.com/CanaKit-Raspberry-Supply-Adapter-Charger/dp/B00MARDJZ4/ref=pd_sim_147_1?_encoding=UTF8&pd_rd_i=B00MARDJZ4&pd_rd_r=16GG90H18DXRBV8JPYC0&pd_rd_w=WuKq5&pd_rd_wg=tjcn6&psc=1&refRID=16GG90H18DXRBV8JPYC0)
- $7.99 [MicroSD Card](https://www.amazon.com/SanDisk-Mobile-MicroSDHC-Adapter-SDSDQM-016G-B35A/dp/B004ZIENBA/ref=sr_1_3?s=pc&ie=UTF8&qid=1493079793&sr=1-3&keywords=micro+sd+card)
- $9.99 [DHT11](https://www.amazon.com/gp/product/B00NAY22V8/ref=oh_aui_detailpage_o07_s01?ie=UTF8&psc=1)
- $30 [Rpi Camera Module](https://www.amazon.com/Raspberry-Pi-Camera-Module-Megapixel/dp/B01ER2SKFS/ref=sr_1_1?s=electronics&ie=UTF8&qid=1493079683&sr=1-1&keywords=pi+cam)
- $3.50 [Light Sensor](https://www.dfrobot.com/product-1004.html?gclid=CI37nLKsvtMCFZIBaQodBhkK3Q)
- $1.86 [Moisture Sensor](https://www.amazon.com/SODIAL-Humidity-Moisture-Detection-Digital/dp/B01I1DNW8O/ref=sr_1_22?s=industrial&ie=UTF8&qid=1493824528&sr=1-22&keywords=moisture+sensor)
- $12.99 [Peristaltic Pump](https://www.amazon.com/ZJchao-Dosing-Peristaltic-Aquarium-Analytic/dp/B00F9MXFFQ/ref=sr_1_5?ie=UTF8&qid=1493824225&sr=8-5&keywords=peristaltic+pump)
- $5.59 [Pump Power supply](https://www.amazon.com/gp/product/B005JRGOCM/ref=oh_aui_detailpage_o02_s01?ie=UTF8&psc=1)
- $3.88 [Silicone Tubing](https://www.amazon.com/Baomain-Silicone-Tubing-Vacuum-Hose/dp/B01IB8EH8S/ref=sr_1_3?s=industrial&ie=UTF8&qid=1493824381&sr=1-3&keywords=white+silicone+tubing+1%2F8%22id)
- $24.99 [LED array](https://www.amazon.com/gp/product/B01IVQ96KY/ref=oh_aui_detailpage_o05_s00?ie=UTF8&psc=1)
- $7.99 [Analog<->Digital Converter](https://www.amazon.com/SMAKN®-PCF8591-Converter-Digital-Conversion/dp/B00RMBTAO2/ref=sr_1_2?s=electronics&ie=UTF8&qid=1493078912&sr=1-2&keywords=PCF8591+AD%2FDA)
- $7.99 [Jumper Wires](https://www.amazon.com/gp/product/B01FPMN432/ref=oh_aui_detailpage_o09_s00?ie=UTF8&psc=1)
- $19.99 [Controllable Outlet](https://www.adafruit.com/product/2935)
- $6.79 [5V Power Relay](https://www.amazon.com/gp/product/B00E0NTPP4/ref=oh_aui_detailpage_o02_s00?ie=UTF8&psc=1)

TOTAL: $188.54

OPTIONAL:
- $19.99 [Socker Enclosure](http://www.ikea.com/us/en/catalog/products/70186603/)
- Ethernet Cable
## Steps
### Setup the Raspberry Pi 3
  1. Format the SD Card.
  2. Downlaod the Linux distribution.
  3. Mount the SD Card.
  4. Put the SD card into the Raspberry Pi 3.
  5. Connect the Raspberry Pi to the internet and find the IP address. 
  6. ssh into the Raspbery Pi 3.
### Setup the SlackBot
  1. Create a slack account and group.
  2. Create a slack bot. 
  3. Connect the slack bot.
### Hardware Setup.
  1. Setup Sensors
     1. Setup the Analog to Digital Converter (ADC for short).
        1. Connect the _ pin of the ADC to the _ pin if the Rpi.
        1. Connect the _ pin of the ADC to the _ pin if the Rpi.
        1. Connect the _ pin of the ADC to the _ pin if the Rpi.
     2. Setup Light Sensor.
        1. Connect the _ pin of the Light Sensor to the _ pin if the Rpi.
        1. Connect the _ pin of the Light Sensor to the _ pin if the Rpi.
        1. Connect the _ pin of the Light Sensor to the _ pin if the Rpi.
     3. Setup Soil Moisture Sensor.
        1. Connect the _ pin of the Soil Moisture Sensor to the _ pin if the Rpi.
        1. Connect the _ pin of the Soil Moisture Sensor to the _ pin if the Rpi.
        1. Connect the _ pin of the Soil Moisture Sensor to the _ pin if the Rpi.
  2. Setup the LED's
     1. Connect left pin to pin _ of the Raspberry Pi.
     2. Connect right pin to pin _ of the Raspberry Pi.
     3. Connect the LED's to the LED power supply.
     4. Plug the LED power supply into the right side of the controlled power source.
  3. Setup the pump
     1. [View the video here!](https://www.youtube.com/watch?v=v65U86tB1cM)
     2. Plug the _ pins of the relay into the 5V pin of the raspberry pi.
     3. Plug the _ pins of the relay into the ground pin of the Raspberry pi.
     4. Put one end of the thick gauge wire into the leftmost terminal of the right relay, screw in to secure.
     5. Wrap the other end to one terminal of the Pump, secure with electrical tape.
     6. Put one end of a different thick gauge wire into the middle terminal of the right relay, screw in to secure.
     7. Secure the other end of the wire onto the 12V source, secure with electrical tape.
     8. Wrap a thick gauge wire around the 12V source ground, secure with electrical tape.
     9. Wrap the other end to the remaining terminal of the Pump.
  4. Setup the Camera
     1. Place the camera strip into the holder facing away from the ethernet port, secure by pressing down on the white.
  
