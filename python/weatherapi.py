import json
import requests

print('Please enter your zip code:')
zip = input()

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=692ecadb2eb7b15991a4698274ae06ab' % zip)
data = r.json()
print(data['weather'][0]['description'])
