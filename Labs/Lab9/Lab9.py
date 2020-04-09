# This is a script to output the name and color of widgets from JSON data.

# Import json and requests to call website and read the data
import json
import requests


# Calling the API created in node
r = requests.get('http://localhost:3000')
data = r.json()

# Creating and printing variable for the first widget
widget1 = (data[0]['name']) +  ' is ' + (data[0]['color'])
print(widget1)

# Creating and printing variable for the second widget
widget2 = (data[1]['name']) + ' is ' + (data[1]['color'])
print(widget2)

# Creating and printing variable for the third widget
widget3 = (data[2]['name']) + ' is ' + (data[2]['color'])
print(widget3)

# Creating and printing variable for the final widget
widgetx = (data[3]['name']) + ' is ' + (data[3]['color'])
print(widgetx)
