class Duck:
    color = "белый"

    def __init__(self, name=None, weight=0):
        self.name = name
        self.weight = weight


    @staticmethod
    def crack():
        print('Crack')

    @classmethod
    def color_duck(cls):
        print(f'Цвет: {cls.color}')


    def show(self):
        print(f'Имя: {self.name}, вес: {self.weight}')

    def __repr__(self):
        if self.name == 'Sum':
            return f'Cуммарный вес уток равен  {self.weight} кг'
        else:
            return f'Утка по имени {self.name} имеет {self.color} цвет и вес в {self.weight} кг'

    def __lt__(self, other):
        return self.weight < other.weight


    def __ne__(self, other):
        return self.weight != other.weight


    def __ge__(self, other):
        return self.weight >= other.weight


    def __eq__(self, other):
        return self.weight == other.weight


    def __add__(self, other):
        return Duck('Sum', self.weight + other.weight)


duck1 = Duck('Ла-ла', 5)
duck1.crack()
duck1.color_duck()
duck1.show()
print(duck1)
duck2 = Duck('Сильва', 4)
print(duck1 > duck2)
print(duck1 + duck2)
