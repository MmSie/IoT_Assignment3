import os
import pandas as pd
import paho.mqtt.client as mqtt
import json
import time
import threading
import sys

# Load JSON data from CSV
csv_file = os.path.expanduser("~/Desktop/abcnews-date-text.csv")
abcnews = pd.read_csv(csv_file, encoding="utf-8")
json_string = abcnews.to_json(orient="records")
json_data = json.loads(json_string)

def send_messages(client):
    for record in json_data:  # Iterate over the records in json_data
        client.publish("your/topic", json.dumps(record))
        print(f"Sent record: {record}")  # Print the sent record
        time.sleep(1)  # Wait for 1 second

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    send_thread = threading.Thread(target=send_messages, args=(client,))
    send_thread.start()

client = mqtt.Client()
client.on_connect = on_connect

client.username_pw_set("username", "password")  # If required
client.connect("127.0.0.1", 1883, 60)

client.loop_start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Interrupted by user, stopping...")
    client.loop_stop()
    sys.exit(0)

