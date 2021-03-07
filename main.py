import json
import requests

URL = 'http://api.nobelprize.org/v1/laureate.json'

r = requests.get(URL)
data_nobel = r.json()
# print(data_nobel)

#a)  wypisze ile łącznie osób otrzymało nagrody
number_prizes = len(data_nobel['laureates'])
print(number_prizes)

