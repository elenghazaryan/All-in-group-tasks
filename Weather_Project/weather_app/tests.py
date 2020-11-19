from django.test import TestCase
import requests

_url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities"
api_key = "98278434e6mshabc873fe683bf71p1284dbjsnc8dbca017e4c"

headers = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': "wft-geo-db.p.rapidapi.com"
}
querystring = {"namePrefix": "E"}

data = requests.get(_url, params=querystring, headers=headers).json()
print(data)
# url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=5240a4be4f6c5130698e4221148b2617"
