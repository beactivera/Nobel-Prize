import requests

URL = 'http://api.nobelprize.org/v1/laureate.json'


class Laureate:
    def __init__(self, firstname, surname, prizes):
        self.firstname = firstname
        self.surname = surname
        self.prizes = prizes

    def __repr__(self):
        return self.firstname + " " + self.surname + " " + str(self.prizes)


def zadanie():
    r = requests.get(URL)
    data_nobel = r.json()
    # print(data_nobel)

    # a)  wypisze ile łącznie osób otrzymało nagrody
    number_prizes = len(data_nobel['laureates'])
    print(f"Ilość osób, które otrzymały Nobla:\n {number_prizes}\n")

    # b) wypisz osoby które otrzymały nagrodę w kategorii  ekonomia ‘economy’ , alfabetycznie
    prize_economy = []

    for laureate in data_nobel['laureates']:
        for prize in laureate['prizes']:
            if prize['category'] == 'economics':
                prize_economy.append(
                    laureate['firstname'] + ' ' + laureate['surname'])  # sortowanie będzie według imienia
                # prize_economy.append(laureate['surname'] + ' ' + laureate['firstname'])
                # sortowanie bedzie według nazwiska
                break
    prize_economy = sorted(prize_economy)
    print(f"Lista osób, które otrzymały nagrodę w dziedzinie ekonomii:\n {prize_economy}\n")

    # c) wypisz osoby które otrzymały nagordę wiecej niż raz wraz z ilością nagród, kolejnośc w zależności
    # od wielokrotności nagrodzenia.
    prize_more_than_one = []

    for laureate in data_nobel['laureates']:
        if len(laureate['prizes']) > 1:
            prize_more_than_one.append(
                Laureate(laureate.get('firstname', ''), laureate.get('surname', ''), len(laureate['prizes'])))

    prize_more_than_one = sorted(prize_more_than_one, key=lambda x: x.prizes, reverse=True)
    print(f"Lista osób/organizacji, które otrzymały więcej niż jedną nagrodę:\n {prize_more_than_one}\n")


zadanie()