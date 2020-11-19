from django.shortcuts import render
import requests
from .example import *


def index(request):
    cities = anunner
    context = {'cities': cities}
    return render(request, 'weather_app/index.html', context)


def info(request, info_id):
    _city = anunner[info_id]
    # __url = "https://community-open-weather-map.p.rapidapi.com/find"
    # __api_key = "98278434e6mshabc873fe683bf71p1284dbjsnc8dbca017e4c"
    k = "5240a4be4f6c5130698e4221148b2617"
    u = f'http://api.openweathermap.org/data/2.5/weather?q={_city}&units=metric&appid={k}'
    # d = f2(__url, __api_key, _city)
    d = requests.get(u).json()
    city_weather = {
        'name': _city,
        'temperature': d['main']['temp'],
        'humidity': d['main']['humidity'],
        'wind': d['wind']['speed'],
        'icon': d['weather'][0]['icon'],
    }

    return render(request, "weather_app/info.html", {
        "city": city_weather
    })

