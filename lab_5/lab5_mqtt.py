"""
Name: Bethany Hamppton
Class: SENG2220 (Computer Organization)
Assignment: Lab 5
Sending JSON data back to a subscriber and include a random temperature every 10 seconds.

"""
import logging
from multiprocessing.connection import wait
import signal
import sys
import json
import random
from time import sleep
from gpiozero import Device, PWMLED
from gpiozero.pins.pigpio import PiGPIOFactory
import paho.mqtt.client as mqtt                                                                # (1)

# Initialize Logging
logging.basicConfig(level=logging.WARNING)  # Global logging configuration
logger = logging.getLogger("main")  # Logger for this module
logger.setLevel(logging.INFO) # Debugging for this file.

# Initialize GPIO
Device.pin_factory = PiGPIOFactory() # Set GPIOZero to use PiGPIO by default.

# Global Variables
LED_GPIO_PIN = 21
BROKER_HOST = "localhost"                                                                       # (2)
BROKER_PORT = 1883
CLIENT_ID = "LEDClient"                                                                         # (3)
TOPIC = "fake_location/fake_sensor/fake_temp"                                                                                 # (4)
client = None  # MQTT client instance. See init_mqtt()   

"""
MQTT Related Functions and Callbacks
"""


def on_connect(client, user_data, flags, connection_result_code):                              # (7)
    """on_connect is called when our program connects to the MQTT Broker.
       Always subscribe to topics in an on_connect() callback.
       This way if a connection is lost, the automatic
       re-connection will also results in the re-subscription occurring."""

    if connection_result_code == 0:                                                            # (8)
        # 0 = successful connection
        logger.info("Connected to MQTT Broker")
    else:
        # connack_string() gives us a user friendly string for a connection code.
        logger.error("Failed to connect to MQTT Broker: " + mqtt.connack_string(connection_result_code))

    # Subscribe to the topic for LED level changes.
    client.subscribe(TOPIC, qos=2)                                                             # (9)


def on_disconnect(client, user_data, disconnection_result_code):                               # (10)
    """Called disconnects from MQTT Broker."""
    logger.error("Disconnected from MQTT Broker")


def on_message(client, userdata, msg):                                   
    #getting payload and converting to string
    payload = str(msg.payload)


    #Making array for location and sensor in order to get a random value each time
    location = ['Main Bedroom', 'Guest Bedroom', 'Bathroom', 'Living Room', 'Garage']
    sensor = ['Sensor 1', 'Sensor 2', 'Sensor 3', 'Sensor 4', 'Sensor 5']
      
    #stting the json data we want to use to a variable (and generating random values from the above arrays)
    #getting a random temperature value using the 'random' import 
    jsonData = {'location': random.choice(location), 'sensor': random.choice(sensor), 'temp': str(random.randint(60,70))}

    # if temp is in the subscribers message then the above json data is then printed 
    # 'temp' also handles 'temperature' should the use input that instead
    # in a nicer format
    if "temp" in payload:
        print(json.dumps(jsonData, indent=4))
        while True: 
            sleep(10)
            print("Updated Temperature: " + str(random.randint(60,70)))
    else:
        print("Unhandled Topic")


def signal_handler(sig, frame):
    """Capture Control+C and disconnect from Broker."""
    logger.info("You pressed Control + C. Shutting down, please wait...")

    client.disconnect() # Graceful disconnection.
    sys.exit(0)

def init_mqtt():
    global client

    # Our MQTT Client. See PAHO documentation for all configurable options.
    # "clean_session=True" means we don"t want Broker to retain QoS 1 and 2 messages
    # for us when we"re offline. You"ll see the "{"session present": 0}" logged when
    # connected.
    client = mqtt.Client(                                                                      # (15)
        client_id=CLIENT_ID,
        clean_session=False)

    # Route Paho logging to Python logging.
    client.enable_logger()                                                                     # (16)

    # Setup callbacks
    client.on_connect = on_connect                                                             # (17)
    client.on_disconnect = on_disconnect
    client.on_message = on_message

    # Connect to Broker.
    client.connect(BROKER_HOST, BROKER_PORT)                                                   # (18)

init_mqtt()


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)  # Capture Control + C                        # (19)
    logger.info("Listening for messages on topic '" + TOPIC + "'. Press Control + C to exit.")

    client.loop_start()                                                                        # (20)
    signal.pause()
