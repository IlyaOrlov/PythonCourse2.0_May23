# Спроектировать классы (один или несколько) для игры в танки и создать экземпляры этих классов.

import random


class Tank:
    list_color = ("Маскировочный летний", "Маскировочный зимний")

    def __init__(self, name="", health="", color=""):
        self.name = name
        self.color = color if color else random.choice(Tank.list_color)
        self.health = health

    def info_tank(self):
        print(f"Модель танка: {self.name} Количество единиц прочности: {self.health} Цвет танка: {self.color}")

T1 = Tank("Т-34","380", "Хаки")
T1.info_tank()

T2 = Tank("КВ-1","400")
T2.info_tank()

T3 = Tank("Абрамс","370")
T3.info_tank()
