# pip3 install requests ipython
# ipython
import requests

# https://www.nylas.com/blog/use-python-requests-module-rest-apis/

response = requests.get("http://api.open-notify.org/astros.json")
print(response)

response.content() # Return the raw bytes of the data payload
response.text() # Return a string representation of the data payload
response.json() # This method is convenient when the API returns JSON


query = {'lat':'45', 'lon':'180'}
response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)
response.json()



