import json
import requests
import googlemaps
from datetime import datetime

#-----------------------------------------------------------------------
#read a json string
my_json_string = '{"fruit": "Apple","size": "Large","color": "Red"}'
output = json.loads(my_json_string)
print(output["size"])


#read json file
with open('sample_json.json') as f:
    data = json.load(f)
print(data)


##convert dict to json
my_dictionary = {
  "name": "John",
  "age": 30,
  "city": "New York"}
output = json.dumps(my_dictionary)
print(output)


#writing a json file
person_dict = {"name": "Bob",
               "languages": ["English", "Fench"],
               "married": True,
               "age": 32}
with open('person.json', 'w') as json_file:
    json.dump(person_dict, json_file)
#-----------------------------------------------------------------------
# GATEWAY API EXAMPLE

#read request body
#the API key is in the body
with open('gateway_body.json') as f:
    request_body = json.load(f)

response = requests.post(url='https://gateway.homolog-interna.4all.com/listTransactions',json=request_body)

# write result as file
with open('gateway_response.json', 'w') as json_file:
    json.dump(response.json(), json_file)
#-----------------------------------------------------------------------
# GOOGLE API EXAMPLE

# POST my API key
gmaps = googlemaps.Client(key='my_key_here')

# GET directions
now = datetime.now()
directions_result = gmaps.directions("R. Dr. Renato Paes de Barros, 1017 - Itaim Bibi, São Paulo - SP, 04530-001",
                                     "Rua Elvira Ferraz, 83 - Itaim Bibi, São Paulo - State of São Paulo",
                                     mode="transit",
                                     departure_time=now)
print(directions_result)

#write result as file
with open('gmaps_result.json', 'w') as json_file:
    json.dump(directions_result, json_file)

#----------------------------


response_login = requests.post(url = 'https://api.twitter.com/oauth2/token',)

response_request = requests.get(url='https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=mggiacometto&count=2')

print(response_request.text)