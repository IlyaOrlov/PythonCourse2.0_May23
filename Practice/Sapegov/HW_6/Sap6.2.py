import random


class Duck:
    c = ('Синяя', 'Желтая', 'Коричневая', 'Белая')
    color = random.choice(c)

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @staticmethod
    def voice():
        print('Crack')

    @classmethod
    def generate_color(cls):
        print(f'Цвет утки: {cls.color}')

    def description(self):
        print(f'Имя утки: {self.name}, Вес: {self.weight} кг')

    def __repr__(self):
        return f'Имя утки: {self.name}, Вес: {self.weight} кг, Цвет утки: {self.color}'

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __ne__(self, other):
        return self.weight != other.weight

    def __add__(self, other):
        res = self.weight + other.weight
        return Duck('Толстушка', res)


d1 = Duck('Крякалка', 10)
d2 = Duck('Синяя шейка', 5)
d3 = Duck('Быстрое крыло', 10)
d4 = Duck('Машка', 15)

d1.voice()
d1.generate_color()
d1.description()
print(d4 < d1)
print(d1 > d2)
print(d3 == d1)
print(d3 != d1)
d5 = d1 + d2
print(d5)
