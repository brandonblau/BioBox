import re
import time
import json
import psutil
import MySQLdb
from slackclient import SlackClient


slack_client = SlackClient("xoxb-154876783414-I2BH4o8xl8io7lnNWbdCXHyc")


# Fetch your Bot's User ID
user_list = slack_client.api_call("users.list")
for user in user_list.get('members'):
    if user.get('name') == "bio-bot":
        slack_user_id = user.get('id')
        break


# Start connection
if slack_client.rtm_connect():
    print "Connected!"

    while True:
        for message in slack_client.rtm_read():
            if 'text' in message and message['text'].startswith("<@%s>" % slack_user_id):

                print "Message received: %s" % json.dumps(message, indent=2)

                message_text = message['text'].\
                    split("<@%s>" % slack_user_id)[1].\
                    strip()

                if re.match(r'.*(water).*', message_text, re.IGNORECASE):
                    cpu_pct = psutil.cpu_percent(interval=1, percpu=False)

		    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                         user="root",         # your username
                         passwd="raspberry",  # your password
                         db="sensor_database")        # name of the data base

                    # you must create a Cursor object. It will let
                    #  you execute all the queries you need
                    cur = db.cursor()

                    # Use all the SQL you like
                    cur.execute("SELECT * FROM plant_log ORDER BY ID DESC LIMIT 1")

                    # print all the first cell of all the rows
                    for row in cur.fetchall():
                        print row[0]

		    db.close()

		    image_url = "/var/www/html/cam.jpg"
		    attachments = attachments = [{"title": "Plant","image_url": image_url}]
	
                    slack_client.api_call(
                        "chat.postMessage",
                        channel=message['channel'],
                        text="My CPU is at %s%%." % cpu_pct,
                        as_user=True,)

                if re.match(r'.*(memory|ram).*', message_text, re.IGNORECASE):
                    mem = psutil.virtual_memory()
                    mem_pct = mem.percent

                    slack_client.api_call(
                        "chat.postMessage",
                        channel=message['channel'],
                        text="My RAM is at %s%%." % mem_pct,
                        as_user=True)

        time.sleep(1)
