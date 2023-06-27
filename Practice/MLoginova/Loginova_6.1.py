import random
import datetime


class Tanks:
    list_country = ("Russia", "USA", "Gourmania", "Ukraine", "Poland")
    PRICE_TANK_USD = 2500000

    def __init__(self, model, country=None):
        self.model = model
        self.country = country if country else random.choice(Tanks.list_country)
        self.price = 0

    @staticmethod
    def price_tank(curs):
        # стоимость танка в рублях(стоимость танка в долларах * на курс)
        price = Tanks.PRICE_TANK_USD * curs
        return price

    def info_tanks(self):
        dt_now = datetime.date.today()
        print(f"Модель {self.model}:\nCтрана {self.country}, стоимость на {dt_now}: {self.price_tank(curs)} руб.\n")


curs = float(input("Enter the course 'USD' for today: "))
t1 = Tanks("T-90")
t1.info_tanks()

t2 = Tanks("Тигр", "Latvia")
t2.info_tanks()

t3 = Tanks("Пантера")
t3.info_tanks()
