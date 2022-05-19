import serial
import paho.mqtt.client as mqtt
import json
import time

TOPIC='/hambetn/Arduino'
#using different serial port because Node-Red is using the ttyS0
ser=serial.Serial("/dev/ttyACM0",9600)  

while True: 
        value = ser.readline().decode('ascii')
        print(value) 



        output = "sensor:Arduino, Temp, " +value
        with open("temps.csv", "a") as fh:
            fh.write(output)
        json_output = {'sensor':'arduino','temperature': value.replace('\n', '')}

        #below is the setup for mqtt to publish to the topic we set
        client = mqtt.Client()
        client.connect("10.43.1.15", 1883, 60)
        client.publish(TOPIC, json.dumps(json_output), qos=0)
        time.sleep(5)
        client.disconnect() 