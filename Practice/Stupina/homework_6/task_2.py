class Duck:
    color = 'brown'

    def __init__(self, name=None, weight=None):
        self.name = name
        self.weight = weight

    @staticmethod
    def crack():
        print('Crack')

    @classmethod
    def color_duck(cls):
        print(f'Цвет утки - {cls.color}')

    def show(self):
        print(f'утка {self.name} весит {self.weight} кг')

    def __repr__(self):
        return f'утка {self.name}\n  цвет: {self.color}  вес: {self.weight} кг'

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __ne__(self, other):
        return self.weight != other.weight

    def __add__(self, other):
        return Duck('Sum', self.weight + other.weight)


d1 = Duck('Дональд', 7)
d1.crack()
d1.color_duck()
d1.show()
print(d1)

d2 = Duck('Серая шейка', 5)
print(d1 != d2)
print(d1 + d2)
