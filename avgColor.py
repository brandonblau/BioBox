from SimpleCV import Color, Image
import curses
import time
import MySQLdb

#Image blocking--block processing

while True:

    img = Image("/var/www/html/cam.jpg");
    width, height = img.size();
    print(str(int(width)) + ' h: ' + str(int(height)));
    color = img.meanColor();
    blue, green, red = img.meanColor();
    red = int(red);
    green = int(green);
    blue = int(blue);

    #Server Connection to MySQL:
    datetime = (time.strftime("%Y-%m-%d ") + time.strftime("%H:%M:%S")) 
    conn = MySQLdb.connect(host= "localhost", user="root", passwd="raspberry", db="sensor_database")
    x = conn.cursor()
    
    #Get last color value:
    try:
        x.execute("SELECT * FROM color_log ORDER BY DATE DESC LIMIT 1;");
        conn.commit()
        row = x.fetchone();
        oldRed = row[1];
        oldGreen = row[2];
        oldBlue = row[3];
    except:
        conn.rollback();

    #Get average daily color value:
    avgRed = 0;
    avgGreen = 0;
    avgBlue = 0;
    length = 0;
    try:
        x.execute("SELECT * FROM color_log WHERE DATE(date)=CURDATE();");
        conn.commit();
        data = x.fetchall();
        
        for rows in data:
            avgRed = (avgRed + rows[1]);
            avgGreen = (avgGreen + rows[2]);
            avgBlue = (avgBlue + rows[3]);
            length = length + 1;

        avgRed = avgRed/length;
        avgGreen = avgGreen/length;
        avgBlue = avgBlue/length;
        
    except:
        conn.rollback();
    
    #insert new color values:
    try:
        x.execute("""INSERT INTO color_log VALUES (%s,%s,%s,%s)""",(datetime,red,green,blue))
        conn.commit()
    except:
        conn.rollback()
    conn.close()   
    #End servier connection


    colorStr = "("+str(red)+","+str(green)+","+str(blue)+")";
    #Draw the average color on the image
    img.drawText(colorStr, x=10, y=height - 20, color= (255, 0, 0), fontsize = 25);
    #print(color);
    #print('Displaying image.  Press return to exit.');
    img.show();
    #raw_input();
    try:
        print('---*Image Captured*---');
        print('Captured Color: ('+str(red)+','+str(green)+','+str(blue)+')');
        print('Color difference: ('+str(oldRed - red)+','+str(oldGreen - green)+','+str(oldBlue - blue)+')');
        print('Daily Color Avg: ('+str(avgRed)+','+str(avgGreen)+','+str(avgBlue)+')');
        print('');
    except:
        pass;
    time.sleep(0.5)


