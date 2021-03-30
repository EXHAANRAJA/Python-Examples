# Getting response from JSON 
import requests
response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()

for people in json['people']:
    print(people['name'])
