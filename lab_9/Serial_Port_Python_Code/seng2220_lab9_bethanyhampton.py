from ast import Return
import json
import paho.mqtt.client as mqtt
import paho.mqtt.publish as mqttPublisher
import serial

BROKER_HOST = "10.43.1.15"                                                                       
BROKER_PORT = 1883
#using 2 topics for led and temperature values
TOPIC_TEMP='/hambetn/temps'
TOPIC_LED = '/hambetn/led'
ser = serial.Serial('/dev/ttyS0', 9600) 

#setting up mqtt connection to lab server
client = mqtt.Client()
client.connect("10.43.1.15", 1883, 60)

#output menu function
#sets user input to a variable 
def get_selection():
    print("1. Get Current Temperature")
    print("2. Turn led on")
    print("3. Turn led off")
    selection = input("Please select one of the above options: ")
    return selection

def main():

    #getting user input
    selection = get_selection()

    #getting temp for option 1
    if (selection == '1'):
        value = ser.readline().decode('ascii')
        print("Temp: ", value) 

        output = "sensor:Arduino, Temp, " +value

        #oringally created a .txt file but swapped to csv for step nine
        #this is creating a csv file and appending to it
        with open("temps.csv", "a") as fh:
             fh.write(output)

        json_output = {'sensor':'arduino','temperature': value.replace('\n', '')}
        
        #publishing to the temperature topic and sending json object payload
        client.publish(TOPIC_TEMP, json.dumps(json_output), qos=0)

    #sending a 1 to turn the led on
    #still trying to configure this portion
    elif (selection == '2'):
       #sending json formatted value to serial output via mqtt
       #sends a string value of 1 to the mqtt broker
       #the Arduino code is reading the ascii charater of this value or a 49 (because in ascii 1 = 49)
             led_on = '{"led": 1}'
             client.publish(TOPIC_LED, led_on, qos=0)
        
    #sending 0 to turn the led off
    #this is also using the same conepts from turning the led on
    elif (selection == '3'):
        led_off = '{"led": "0"}'
        client.publish(TOPIC_LED, led_off, qos=0)

    #no other selections would be valid 
    #prompting the user to enter a valid input
    else:
        print("Please enter a valid selection")

    #disconnect client
    client.disconnect()

main()