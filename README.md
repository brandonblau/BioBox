# ![BioBox](https://github.com/brandonblau/BioBox/blob/master/Resources/BioBoxLogoSmall.jpg?raw=true)
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
#### MacOS SD Card Intall:
[Tutorial from here](https://computers.tutsplus.com/articles/how-to-clone-raspberry-pi-sd-cards-using-the-command-line-in-os-x--mac-59911)
 1. Download Software Image from [here] 
 2. Insert the MicroSD Card to be installed upon
- Insert a blank (or used and nuked) SD card into the SD card reader on your Mac.
 3. Locate the MicroSD Card to be used
- Open Terminal and locate your MicroSD card, noting that the number may be different than shown below:
		diskutil list
	![pic1](https://github.com/brandonblau/BioBox/blob/master/Resources/pic1.png?raw=true)
 4. Unmount the MicroSD Card
- In Terminal, enter the following command:
		diskutil unmountDisk /dev/disk2
 5. Format the MicroSD Card
- When you have identified your MicroSD Card, enter the following command to format it as FAT16, in my case its /dev/disk2.  Amend this as required for your circumstances:
		sudo newfs_msdos -F 16 /dev/disk2
	![pic2](https://github.com/brandonblau/BioBox/blob/master/Resources/pic2.png?raw=true)
6. Install from the downloaded Disc Image
- Locate the disc image, .dmg, that you previously downed. My example assumes that the dmg is on the Desktop. In Terminal, enter the following command ensuring that you identify the correct destination disc, in my example it’s /dev/disk2.
		sudo dd if=~/Desktop/raspberrypi.dmg of=/dev/disk2 
	![pic3](https://github.com/brandonblau/BioBox/blob/master/Resources/pic3.png?raw=true)
Tip: Be aware that restoring the disc image to the SD Card can take some time. Probably a lot longer than you think. My Mac took 3 hours 27 minutes to restore on an 16GB SDXC card.

#### Windows SD Card Install
Download Win32DiskImager from [here](http://sourceforge.net/projects/win32diskimager/)
Download BioBoxOS Image from [here]()

1. Insert the SD card back into your computer.
2. Head to the start menu or screen and type "disk management." Open the disk management program and find your SD card in the list.
3. Right-click and delete all the partitions on your SD card. When it's empty, right-click on it and format it (it doesn't matter what filesystem you format it to, your computer just needs to recognize it).
4. Open Win32DiskImager again and browse for your image file. Select your device from the Device dropdown just as you did before.
5. Click "Write" to write the image to the SD card.
6. When it finishes, eject the SD card and re-insert it into your Raspberry Pi. When you boot it up, it should be in the exact same state it was in when you first cloned the SD card.

### Download software and dependencies.
  1. Put the SD card into the Raspberry Pi 3.
  2. Connect the Raspberry Pi to the internet and find the IP address. 
  3. ssh into the Raspbery Pi 3.
### Setup the SlackBot
  1. [Create a slack account and group.](https://slack.com/get-started)
  2. [Create a slack bot and save the key.](https://my.slack.com/services/new/bot) 
  3. Connect the slack bot.
### Set Software Preferences for BioBox
  1. On any web-browser, connect to your BioBox's IP address
  - Our's, for instance, is at 10.5.96.104
  2. For safety and security, the BioBox page is password protected.  
  - By default: Username: biobox  Password: biobox
  - ![screencap](https://github.com/brandonblau/BioBox/blob/master/Resources/screencap.png?raw=true)
  - Here is where you can view your plant from your home network, take pictures or videos, and save the pictures and video to your computer.
  - ![landingpageScreencap](https://github.com/brandonblau/BioBox/blob/master/Resources/landingpageScreencap.png?raw=true)
  3. Select "Customization Settings" from the top navigation bar
  - This is where you tell the system the color of the plant you are growing for image processing detection, the amount of time you want the plant to have light.  What time you want the light to start. The contact frequency of the emailing system, and the place where you input the key generated for your specific SlackBot in the previous step.  
  - ![customizationScreenCap](https://github.com/brandonblau/BioBox/blob/master/Resources/customizationScreenCap.png?raw=true)
  - Hardware specification settings are advanced and are how the system knows which sensors are connected where on the Raspberry Pi.  Super Useres only should change these settings.  
  
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
  
