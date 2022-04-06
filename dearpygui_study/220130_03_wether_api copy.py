# cd dearpygui_study
# python3
import requests
import json

with open("secret.json", "r") as json_file:
    secret = json.load(json_file)

# api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

query = {'q':'Sao Paulo', 'appid':secret["openwether"]["api-key"]}

response = requests.get('http://api.openweathermap.org/data/2.5/weather', params=query)
json_response = response.json()

# to transform temperature from Kelvin to Celsius
# -273.15



