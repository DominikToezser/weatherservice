import requests
import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

URL = "https://api.weather.com/v3/location/near?"

PARAMS = {
    'geocode':'33.74,-84.39',
    'product':'airport',
    'format':'json',
    'apiKey':'915228bace4849709228bace48097056',
}


response = requests.get(url = URL , params = PARAMS)

#"https://api.weather.com/v3/location/near?geocode=33.74,-84.39&product=airport&format=json&apiKey=915228bace4849709228bace48097056"

jprint(response.json())

"""jprint(response.json())"""
