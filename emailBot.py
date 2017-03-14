import smtplib
import time
import email
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

def sendEmail(stringIn):
        
    fromaddr = "bioboxdev@gmail.com"
    toaddr = "brandonblau@me.com"
     
    msg = MIMEMultipart()
     
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Biobox water update"+time.strftime(" %Y-%m-%d ") + time.strftime("%H:%M:%S")
     
    body = stringIn
     
    msg.attach(MIMEText(body, 'plain'))
     
    filename = "cam.jpg"
    attachment = open("/var/www/html/cam.jpg", "rb")
     
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
     
    msg.attach(part)
     
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "tinyrick")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

sendEmail("This is testing the string in function!")
