import requests
import json
import os
from datetime import datetime


city_code_taiyuan = 101180101
url = f'http://t.weather.sojson.com/api/weather/city/{city_code_taiyuan}'
resp = requests.get(url=url)
if resp.status_code == 200:
    resp_json = resp.text

    print(resp_json)