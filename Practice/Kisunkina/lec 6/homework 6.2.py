# Спроектировать класс Duck, при создании экземпляров которого будут задаваться атрибуты
# name, weight, а атрибут color должен быть общим для всех экземпляров класса. Также в классе
# должны быть методы:
# - статический метод, выводящий «Сrack»;
# - классовый метод, выводящий цвет уток;
# - методы экземпляров: метод, выводящий имя и вес утки;
# метод __repr__ ;
# методы сравнения уток по весу (>, <, ==, !=), возвращающие значение
# типа bool (__lt__, __gt__, __eq__, __ne__);
# метод, принимающий 2-х уток и возвращающий утку, вес которой равен сумме весов 2-х уток (__add__).

class Duck:
    color = "Жёлтая"

    def __init__(self, name=None, weight=0):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f"Привет, я уточка {self.name}, мой вес {self.weight} кг."

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __ne__(self, other):
        return self.weight != other.weight

    def __add__(self, other):
        sum_duck = self.weight + other.weight
        return Duck("Шварцнейгер", sum_duck)

    @staticmethod
    def saycrack():
        print("Сrack")

    @classmethod
    def mycolor(cls):
        print(f"Мой цвет: {cls.color}.")

d1 = Duck("Бандерос", 3)
d2 = Duck("Белуччи", 2)

Duck.saycrack()
Duck.mycolor()

print(d1)
print(d2)

sum_duck = d1 + d2
print(f"Третья утка: {sum_duck}")
print("======================")
print("Сравним уток по весу")
print(f"Больше ли утка Бандерос по сравнению с Белуччи {d1 > d2}")
print(f"Меньше ли утка Бандерос по сравнению с Белуччи {d1 < d2}")
print(f"Равны ли по весу утки Бандерос и Белуччи {d1 == d2}")
print(f"Не равны ли по весу утки Бандерос и Белуччи {d1 != d2}")