# Event-driven Home Application - Project Group 3
## Course: Event-driven and Process-oriented Applications for IoT
## University of St. Gallen

### Group Members:
- Marc Sieber
- Alexander Bertignol

### Assignment 3

The aim of this project is to implement an event-driven application for a simulated home environment.

#### Project Overview:

The project is split into two main parts:

1. **Data Generation** - We generate sensor data to simulate brightness and temperature conditions throughout a year. The data generation process factors in daily changes as well as seasonal variations. These scripts can be found in `main.ipynb`.

2. **MQTT Client** - We use the Paho MQTT client to send the generated data to an MQTT broker. The sensor data is loaded from CSV files and sent to the broker in JSON format with a defined delay to simulate real-time data transmission. This script can be found in `main.py`.

#### Instructions:

1. Run the scripts in `main.ipynb` to generate brightness and temperature sensor data for a full year. The generated data will be saved as CSV files on your desktop.

2. Run `main.py` to start sending the sensor data to the MQTT broker. 

Please note: You need to have `pandas`, `paho-mqtt`, `numpy`, `astral`, `os`, `datetime` and `json` Python libraries installed to run these scripts.

#### Data for Demo Video:

The data used in the demo video is available in this repository. You can find the following CSV files here:

- `brightness_sensor_data_full_year.csv`
- `temperature_sensor_data_full_year.csv`

#### Visualisations in main.ipynb:

The `main.ipynb` file also contains visualisations that describe the seasonal and daily variations temperature.
