def getSetting(index, path):
	#/home/pi/Desktop/settings.txt
	#0->plant  1->lighthour 2->lightstart
	#3->maxwater 4->emailto 5->emailfreq
	#6->slack 7->emailfrom 8->emailfrompass

	f = open(path, 'r');
	settings=[]
	for line in f:
		words = line.split()
		settings.append(words[1])
	f.close()
	return settings[index]

def editSetting(index, path, newSetting):
        #/home/pi/Desktop/settings.txt
	#0->plant  1->lighthour 2->lightstart
	#3->maxwater 4->emailto 5->emailfreq
	#6->slack 7->emailfrom 8->emailfrompass
        
        f = open(path, 'r+');
	lines = f.readlines();
	for i, line in enumerate(lines):
                words=line.split();
                print line
                if words[0] == 'maxwater':
                        string = words[0]+' '+str(newSetting);
                        lines.insert(i,string)
                        print 'edited'
        f.truncate(0)
        f.seek(0)
        f.writelines(lines)
        print 'success'
        f.close()

#first setup the file:
#input = raw_input("Would you like to change the existing settings? (y/n): ");
#if (input == 'y' or input == 'Y'):
	#do something
	#print 'yay'

#------------Retreive settings from file--------------
#print "Installing from previous settings..."
#f = open('/home/pi/Desktop/settings.txt', 'r');

#settings=[]
#for line in f:
	#print line
	#words = line.split()
	#settings.append(words[1])

#f.close()
#print settings


	
