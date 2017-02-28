from SimpleCV import *
import time;

img = Image("/var/www/html/cam.jpg");
hue = img.hueDistance(Color.GREEN);
output = img.edges(t1 = 0);

#hue.show();
output.show();
raw_input();

blobs = img.findBlobs();

#for b in blobs:
#    test = img.crop(b)
#    test.show();
#    time.sleep(0.5);

hue.show();
time.sleep(5);

