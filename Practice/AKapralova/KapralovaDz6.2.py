class Duck:
    color = "Серая"

    def __init__(self, name1, weight1):
        self.name = name1
        self.weight = weight1

    def __repr__(self):
        print(f"Привет, меня зовут уточка {self.name}, мой вес: {self.weight} кг.")

    def __lt__(self, other):  # Меньше чем
        return self.weight < other.weight

    def __gt__(self, other):  # Больше чем
        return self.weight > other.weight

    def __eq__(self, other):  # Равенство
        return self.weight == other.weight

    def __ne__(self, other):  # Неравенство
        return self.weight != other.weight

    def __add__(self, other):
        summa = self.weight + other.weight
        return summa

    @staticmethod
    def say():
        print("Сrack")

    @classmethod
    def mycolor(cls):
        print(f"Мой цвет: {cls.color}.")


d1 = Duck("Поночка", "3")
d1.__repr__()
d1.say()
d1.mycolor()

d2 = Duck("Лапочка", "5")
d2.__repr__()
d2.say()
d1.mycolor()

print(d2 < d1)
print(d2 > d1)
print(d2 == d1)
print(d2 != d1)
d3 = d1 + d2
print(f"Общий вес уток: {d3}")
