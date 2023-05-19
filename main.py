import os
import pandas as pd
import paho.mqtt.client as mqtt
import json
import time
import threading
import sys

# Load JSON data from CSV
brightness_csv_file = os.path.expanduser("~/Desktop/brightness_sensor_data_full_year.csv")
brightness_data = pd.read_csv(brightness_csv_file, encoding="utf-8")
brightness_json_string = brightness_data.to_json(orient="records")
brightness_json_data = json.loads(brightness_json_string)

temperature_csv_file = os.path.expanduser("~/Desktop/temperature_sensor_data_full_year.csv")
temperature_data = pd.read_csv(temperature_csv_file, encoding="utf-8")
temperature_json_string = temperature_data.to_json(orient="records")
temperature_json_data = json.loads(temperature_json_string)

# Define a function for sending records with a delay
def send_messages(client):
    for brightness_record, temperature_record in zip(brightness_json_data, temperature_json_data):
        client.publish("storage/brightness", json.dumps(brightness_record))
        print(f"Sent brightness record: {brightness_record}")
        time.sleep(1)
        client.publish("storage/temperature", json.dumps(temperature_record))
        print(f"Sent temperature record: {temperature_record}")
        time.sleep(1)

# Define a function to check connection with the MQTT client and create a thread to call the send function defined above
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    send_thread = threading.Thread(target=send_messages, args=(client,))
    send_thread.start()

# Create an instance of the MQTT client class
client = mqtt.Client()
# Run the function on_connect for the created client
client.on_connect = on_connect

# Insert the connection details
client.username_pw_set("ftsim", "unisg")
client.connect("ftsim.weber.ics.unisg.ch", 1883, 60)

# Start the MQTT loop in a new thread
client.loop_start()

# This is a loop that runs indefinitely
try:
    while True:
        time.sleep(1)
# If the user interrupts the program the following code will be executed
except KeyboardInterrupt:
    print("Interrupted by user, stopping...")
    # Stop the MQTT loop
    client.loop_stop()
    sys.exit(0)