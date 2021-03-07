import json
import requests

URL = 'http://api.nobelprize.org/v1/laureate.json'

r = requests.get(URL)
data_nobel = r.json()
print(data_nobel)


