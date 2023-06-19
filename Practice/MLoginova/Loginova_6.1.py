import random
import datetime

class Tanks:
    model = "_"
    country = "_"
    price = 0

    def __init__(self, model_):
        self.model = model_
        self.country = "_"
        self.price = 0

    def random_country(self, list_country):
        country = random.choice(list_country)
        return country

    #стоимость танка в рублях(стоимость танка в долларах * на курс)
    def price_tank(self, kurs_usd):
        price = PRICE_TANK_USD * kurs_usd
        return price

    def info_tanks(self):
        dt_now = datetime.date.today()
        print(f"Модель танка {self.model}:\nCтрана {self.random_country(list_country)}, стоимость на дату {dt_now} в рублях: {self.price_tank(kurs_usd)}.\n")


list_country = ["Russia", "USA", "Gourmania", "Ukraine", "Poland"]
# пока не знаю как курс взять с сайта ЦБ РФ, пусть его введёт пользователь для дальнейшего расчёта стоимости танка в руб.:
kurs_usd = float(input("Enter the course 'USD' for today: "))
PRICE_TANK_USD = 2500000

t1 = Tanks("T-90")
t1.info_tanks()

t2 = Tanks("Тигр")
t2.info_tanks()

t3 = Tanks("Пантера")
t3.info_tanks()
