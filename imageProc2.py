#from SimpleCV import Color, Image, *
from SimpleCV import *
import curses
import time
import MySQLdb

sensitivity = 100;    #sensitivity.  Higher (cap 255): less sensitive to hue changes. 

img = Image("/var/www/html/cam.jpg");
width, height = img.size();
xnum = 512;
ynum = 288;
xwidth = 1;
ywidth = 1;
img_copy = Image("/var/www/html/cam.jpg");

peaks = img.huePeaks();
#hue = img.hueDistance(peaks[0][0]);
hue = img.hueDistance(Color.GREEN);

good=0;
bad=0;

for n in range(0, 512*288):
    x = n % 512;
    y = int(n/288);
    crop = hue.crop(x*xwidth, y*ywidth, w=1, h=1, centered=False);
    newlayer = DrawingLayer(img.size());
    
    assignedColor = Color.GREEN;
    good = good +1;
    blue, red, green = crop.meanColor();
    avg = (red+blue+green)/3;
    if avg > sensitivity:
        assignedColor = Color.RED;
        good = good - 1;
        bad = bad + 1;
    img_copy.dl().rectangle((x*xwidth,y*ywidth), (xwidth,ywidth), color = assignedColor, filled=True, alpha = 100);

    #img_copy.show()
    #time.sleep(0.1);

print('There are '+str(good)+' detected plant divisions and '+str(bad)+' non-plant divisions');
img_copy.show();
time.sleep(2);

hue.show();
time.sleep(4);
