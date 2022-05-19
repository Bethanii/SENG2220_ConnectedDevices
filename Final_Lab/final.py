# --SHORT IMPORT DESCRIPTIONS--

#Busio- supports SPI protocols 
#Diigitalio- Provides access to I/O 
#Board- Container for board pin names
#Adafruit_mcp3xxx-library for dealing with ADCs (analog to digital converters) with the msp3008 microchip
#Mqtt- library for puclisher and client handling for mqtt protocol
#Json - library for working with json data
#Time - library for working with time

import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import paho.mqtt.client as mqtt
import paho.mqtt.publish as mqttPublisher
import json
import time
import serial

#the below code is setting the correct serial perpheral interfaces
#mathcing the correct pins on the pi with the correct pins on the mcp3008
#after these connections are made channel is set to the recieved analog value
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D5)
mcp = MCP.MCP3008(spi, cs)
channel = AnalogIn(mcp, MCP.P0)

#ARDUINO CONFIGURATION
ser = serial.Serial('/dev/ttyS0', 9600) 

BROKER_HOST = "10.43.1.15"                                                                       
BROKER_PORT = 1883
#temperature values will be published to the below topic on node-red
TOPIC_Arduino= '/hambetn/Arduino'
TOPIC_MCP='/hambetn/mcp3008'

#setting up mqtt connection to lab server
client = mqtt.Client()
client.connect("10.43.1.15", 1883, 60)

#converting from voltage to fahrenheit
voltage = channel.voltage
tempC = (voltage - 0.5)*100
tempF = (tempC * 9.0/5.0)+32.0
tempF = round(tempF, 3)
json_temp = {"Temp": tempF}

#while loop continuously gets the raw adc value
#also continuously gets voltage and temperature3343790412
#displays these values to the command line and also publishes these to node-red

'''-------------ADC TEMPERATURE----------------------'''
while True:
    print('Raw ADC Value: ', channel.value)
    print('ADC Voltage: ' + str(voltage) + 'V')
    print("Temperature in F: ", tempF)
    
    #publishing temperature readings in json format to node-red
    client.publish(TOPIC_MCP, json.dumps(json_temp), qos=0)
    time.sleep(5)

'''------------ARDUINO TEMPERATURE------------------'''



client.disconnect()