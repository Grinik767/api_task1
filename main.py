import sys
from io import BytesIO
from func import zoom_toponym

import requests
from PIL import Image

toponym_to_find = " ".join(sys.argv[1:])

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}

response = requests.get(geocoder_api_server, params=geocoder_params)

if not response:
    pass
else:
    json_response = response.json()

    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    with open('test.json', 'w', encoding='utf-8') as f:
        f.write(str(toponym))
    lc = toponym['boundedBy']['Envelope']['lowerCorner']
    uc = toponym['boundedBy']['Envelope']['upperCorner']

    toponym_coodrinates = toponym["Point"]["pos"].split()
    toponym_longitude, toponym_lattitude = toponym_coodrinates

    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": zoom_toponym(lc, uc),
        "l": "map",
        "pt": f'{",".join(toponym_coodrinates)},pm2dbl'
    }
    map_api_server = "http://static-maps.yandex.ru/1.x/"

    response = requests.get(map_api_server, params=map_params)

    Image.open(BytesIO(
        response.content)).show()
