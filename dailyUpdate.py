from sql import avgDailyValue
import smtplib
import time
import email
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders


fromaddr = "bioboxdev@gmail.com"
toaddr = "brandonblau@me.com"
     
msg = MIMEMultipart()
     
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Biobox daily update"+time.strftime(" %Y-%m-%d ")
     
line1 = '  Biobox dailyupdate ' + time.strftime(" %Y-%m-%d ")
line2 = '------------------------------------'
line3 = 'Average temp: ' + str(avgDailyValue("Temp"))
line4 = 'Average light: ' + str(avgDailyValue("Light"))
line5 = 'Average moisture: ' + str(avgDailyValue("Moist"))
line6 = 'Average humidity: ' + str(avgDailyValue("Humidity"))
line7 = 'Average watered: ' + str(avgDailyValue("Watered"))
body = line1 + '/r' + line2 + '/r' + line3 + line4 + '/r'  + line5 + '/r'  + line6 + '/r'  + line7

msg.attach(MIMEText(body, 'plain'))
     
filename = "cam.jpg"
     
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "tinyrick")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

