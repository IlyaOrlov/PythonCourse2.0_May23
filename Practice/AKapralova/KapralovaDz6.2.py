class Duck:
    color = "Серая"

    def __init__(self, name1, weight1):
        self.name = name1
        self.weight = weight1

    def __repr__(self):
        return f"{self.name} {self.weight}"

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
        return Duck('Помпушка', summa)

    @staticmethod
    def say():
        print("Сrack")

    @classmethod
    def mycolor(cls):
        print(f"Мой цвет: {cls.color}.")


d1 = Duck("Поночка", 3)
print(f"Привет, меня зовут уточка {d1.name}, мой вес {d1.weight} кг.")
d1.say()
d1.mycolor()

d2 = Duck("Лапочка", 5)
print(f"Привет, меня зовут уточка {d2.name}, мой вес {d2.weight} кг.")
d2.say()
d1.mycolor()

print(d2 < d1)
print(d2 > d1)
print(d2 == d1)
print(d2 != d1)
d3 = d1 + d2
print(f"Самая аппетитная уточка: {d3} кг.")
