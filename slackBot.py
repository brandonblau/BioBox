import websocket
import emailBot
import re
import time
import json
import psutil
import MySQLdb
from slackclient import SlackClient


tempCol = 1;
lightCol = 2;
moistCol = 3;
humidCol = 4;
waterCol = 5;


slack_client = SlackClient("xoxb-154876783414-I2BH4o8xl8io7lnNWbdCXHyc")


# Fetch your Bot's User ID
user_list = slack_client.api_call("users.list")
for user in user_list.get('members'):
    if user.get('name') == "bio-bot":
        slack_user_id = user.get('id')
        break


# Start connection
if slack_client.rtm_connect():
    #print "Connected!"
    count = 0;
    while count < 5:
        for message in slack_client.rtm_read():
            if 'text' in message and message['text'].startswith("<@%s>" % slack_user_id):
                #print "Message received: %s" % json.dumps(message, indent=2)

                message_text = message['text'].\
                    split("<@%s>" % slack_user_id)[1].\
                    strip()

                db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                         user="root",         # your username
                         passwd="raspberry",  # your password
                         db="sensor_database")        # name of the data base

                cur = db.cursor()

                # Use all the SQL you like
                cur.execute("SELECT * FROM plant_log ORDER BY DateTime DESC LIMIT 1")
                    
                row = cur.fetchone()

                db.close()

                if re.match(r'.*(cpu).*', message_text, re.IGNORECASE):
                    cpu_pct = psutil.cpu_percent(interval=1, percpu=False)
                    slack_client.api_call(
                        "chat.postMessage",
                        channel=message['channel'],
                        text="My temperature is at {0}%.".format(cpu_pct),
                        as_user=True,)

                if re.match(r'.*(temperature|temp).*', message_text, re.IGNORECASE):
                    slack_client.api_call(
                        "chat.postMessage",
                        channel=message['channel'],
                        text="My temperature is at {0} F.".format(row[tempCol]),
                        as_user=True,)

                if re.match(r'.*(light|leds).*', message_text, re.IGNORECASE):

                    slack_client.api_call(
                        "chat.postMessage",
                        channel=message['channel'],
                        text="My light is at {0}.".format(row[lightCol]),
                        as_user=True,)

                if re.match(r'.*(moisture|moist).*', message_text, re.IGNORECASE):
                    slack_client.api_call(
                        "chat.postMessage",
                        channel=message['channel'],
                        text="My moisture is at {0}%.".format(row[moistCol]),
                        as_user=True,)

                if re.match(r'.*(humid|humidity).*', message_text, re.IGNORECASE):
                    slack_client.api_call(
                        "chat.postMessage",
                        channel=message['channel'],
                        text="My humidity is at {0}%.".format(row[humidCol]),
                        as_user=True,)

                if re.match(r'.*(watered|water|pump).*', message_text, re.IGNORECASE):
                    slack_client.api_call(
                        "chat.postMessage",
                        channel=message['channel'],
                        text="My pump is {0}.".format(row[waterCol]),
                        as_user=True,)
                if re.match(r'.*(asghari).*', message_text, re.IGNORECASE):
                    slack_client.api_call(
                        "chat.postMessage",
                        channel=message['channel'],
                        text="Wo0o0o0o0o0o0o0o0o0o0o0ow.....",
                        as_user=True,)
                if re.match(r'.*(picture|email).*', message_text, re.IGNORECASE):
                    userID = message['user'];
                    email = "";
                    for user in user_list.get('members'):
                        if user.get('id') == userID:
                            email = user.get('profile').get('email');
                            break;
                    slack_client.api_call(
                        "chat.postMessage",
                        channel=message['channel'],
                        text="sending a picture to " + email,
                        as_user=True,)
                    emailBot.sendPicEmail("Here is a picture",email);
            count += 1;
	    print count;
