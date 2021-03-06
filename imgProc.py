#from SimpleCV import Color, Image, *
from SimpleCV import *
import curses
import time
import MySQLdb

sensitivity = 100;    #sensitivity.  Higher (cap 255): less sensitive to hue changes. 

img = Image("/var/www/html/cam.jpg");
width, height = img.size();
square = 50;
xwidth = width/square;
ywidth = height/square;
img_copy = Image("/var/www/html/cam.jpg");

#peaks = img.huePeaks();
#hue = img.hueDistance(peaks[0][0]);
hue = img.hueDistance(Color.GREEN);

good=0;
bad=0;

firstx = (img.width/3)
firsty = (img.height)
print(img.width)
print(img.height)

crop = img.crop(0, 0, w=firstx, h=firsty, centered=False);
crop.show()
time.sleep(0.3)

for n in range(0, square*square):
    x = n % square;
    y = int(n/square);
    crop = hue.crop(x*xwidth, y*ywidth, w=width/square, h=height/square, centered=False);

    newlayer = DrawingLayer(img.size());
    
    assignedColor = Color.WHITE;
    good = good +1;
    blue, red, green = crop.meanColor();
    avg = (red+blue+green)/3;

    if avg > sensitivity:
        assignedColor = Color.BLACK;
        good = good - 1;
        bad = bad + 1;
        img_copy.dl().rectangle((x*xwidth,y*ywidth), (xwidth,ywidth), color = assignedColor, filled=True, alpha = 255);


print('There are '+str(good)+' detected plant divisions and '+str(bad)+' non-plant divisions');
img_copy.show();
time.sleep(2);

hue.show();
time.sleep(2);
