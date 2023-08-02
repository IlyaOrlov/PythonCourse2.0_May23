import random


class Duck:
    col = ("Белая", "Серая", "Черная")
    color = random.choice(col)

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @staticmethod
    def crack():
        print("Crack")

    @classmethod
    def duck_color(cls):
        return cls.color

    def __repr__(self):
        return f"{self.__class__}: {self.name}"

    def show_duck(self):
        return f"{self.name=}, {self.weight=}"

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
        return sum_duck


d1 = Duck("Gus", 300)
d2 = Duck("Mike", 500)
print(d1.__repr__())
