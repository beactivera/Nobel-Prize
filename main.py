import json
import requests

URL = 'http://api.nobelprize.org/v1/laureate.json'

r = requests.get(URL)
data_nobel = r.json()
# print(data_nobel)

#a)  wypisze ile łącznie osób otrzymało nagrody
number_prizes = len(data_nobel['laureates'])
# print(number_prizes)

#b) wypisz osoby które otrzymały nagrodę w kategorii  ekonomia ‘economy’ , alfabetycznie
prize_economy = []

for laureate in data_nobel['laureates']:
    # print(laureate['prizes'])
    for prize in laureate['prizes']:
        if prize['category'] == 'economics':
            prize_economy.append(laureate['firstname'] + ' ' + laureate['surname']) #sortowanie będzie według imienia
            # prize_economy.append(laureate['surname'] + ' ' + laureate['firstname']) #sortowanie bedzie według nazwiska
            break
prize_economy = sorted(prize_economy)
print(prize_economy)





