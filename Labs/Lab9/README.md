# Lab 9
This lab is a script that sends output of widget name and color from a webpage using a json file.

## Code to import json and requests to get the data
```
import json
import requests
```

## Call the API created in node
```
r = requests.get('http://localhost:3000')
data = r.json()
```

## Creating and printing variables displaying name and color of widget
```
widget1 = (data[0]['name']) + ' is ' + (data[0]['color'])
print(widget1)
```
Duplicate that code swapping out 'widget1' for widget2, widget3, and widgetx.
Also swap out the [0] in the variable for [1], [2], and [3].

## Sample Output
```
widget1 is blue
widget2 is green
widget3 is black
widgetX is blue
```
