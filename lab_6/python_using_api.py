#Name: Bethany Hampton
#Class: SENG2220
#Assignment: Lab 6


import requests


#getting data from my database
r = requests.get('http://10.43.2.9:1880/MongoDB').json()


#variable temp_data stores the returned data as JSON
#in Python, JSON data like {name:value,name:value,name:value...} is treated like a "dictionary"
temp_data = r.json()


#header
print("Bethany's first five temps: ")

#printing out the first five temps
#this is done with a for loop
for i in range(5):
    #setting temp to i index
    value = temp_data[i]["temp"]

print(value)