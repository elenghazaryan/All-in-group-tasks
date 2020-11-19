import requests


# def f(_url, _api_key, _city_name):
#     query_params = {
#         'q': _city_name.startswith("E"),
#         'appid': _api_key,
#     }
#
#     data = requests.get(url=_url, params=query_params).json()
#     return data


def f2(_url, _api_key, _city):
    querystring = {
        "q": _city
    }

    headers = {
        'x-rapidapi-key': _api_key,
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }

    data = requests.get(_url, headers=headers, params=querystring).json()
    return data


def f3(_url, _api_key, _name_prefix, _limit=10):
    _url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities"

    querystring = {"limit": 10, "namePrefix": "E"}

    headers = {
        'x-rapidapi-key': "98278434e6mshabc873fe683bf71p1284dbjsnc8dbca017e4c",
        'x-rapidapi-host': "wft-geo-db.p.rapidapi.com"
    }

    # querystring = {
    #     'limit': _limit,
    #     'namePrefix': _name_prefix
    # }
    #
    # headers = {
    #     'x-rapidapi-key': _api_key,
    #     'x-rapidapi-host': "wft-geo-db.p.rapidapi.com"
    # }

    data = requests.get(_url, headers=headers, params=querystring).json()['data']
    names = []
    for city in data:
        names.append(city['name'])
    return names



url = "https://community-open-weather-map.p.rapidapi.com/find"
api_key = "98278434e6mshabc873fe683bf71p1284dbjsnc8dbca017e4c"
# api_key2 = "5240a4be4f6c5130698e4221148b2617"
# print(f(url, api_key, city))
anunner = f3(7, 7, 7, 7)
print(anunner)
for anun in anunner:
    print(f2(url, api_key, anun))
