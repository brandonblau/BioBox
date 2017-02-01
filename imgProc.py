#from SimpleCV import Color, Image, *
from SimpleCV import *
import curses
import time
import MySQLdb

img = Image("/var/www/html/cam.jpg");
width, height = img.size();
square = 64;
xwidth = width/square;
ywidth = height/square;
img_copy = Image("/var/www/html/cam.jpg");

peaks = img.huePeaks();
hue = img.hueDistance(peaks[0][0]);

good=0;
bad=0;

for n in range(0, square*square):
    x = n % square;
    y = int(n/square);
    crop = hue.crop(x*xwidth, y*ywidth, w=width/square, h=height/square, centered=False);
    newlayer = DrawingLayer(img.size());
    
    assignedColor = Color.GREEN;
    good = good +1;
    blue, red, green = crop.meanColor();
    avg = (red+blue+green)/3;
    if avg > 100:
        assignedColor = Color.RED;
        good = good - 1;
        bad = bad + 1;
    img_copy.dl().rectangle((x*xwidth,y*ywidth), (xwidth,ywidth), color = assignedColor, filled=True, alpha = 150);

    #img_copy.show()
    #time.sleep(0.1);

print('There are '+str(good)+' good divisions and '+str(bad)+' bad divisions');
avg2 = (good /(good+bad) ) 
print('giving '+str( avg2 )+'%');
img_copy.show();
time.sleep(2);



hue.show();
time.sleep(4);
