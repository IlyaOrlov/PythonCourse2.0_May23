class Duck:
    color = "коричневый"  # Общий атрибут color для всех экземпляров класса

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @staticmethod
    def quack():
        print("Crack")

    @classmethod
    def get_color(cls):
        print(f"Цвет утки - {cls.color}")

    def display_info(self):
        print(f"Имя: {self.name}, Вес: {self.weight} кг")

    def __repr__(self):
        return f"Утка(имя={self.name}, вес={self.weight})"

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __ne__(self, other):
        return self.weight != other.weight

    def __add__(self, other):
        new_weight = self.weight + other.weight
        return Duck("Дональд Серошейный", new_weight)


duck1 = Duck("Серая шейка", 1.5)
duck2 = Duck("Дональд", 2.0)

# Вызов статического метода
Duck.quack()

# Вызов классового метода
Duck.get_color()

# Вызов методов экземпляров
duck1.display_info()
duck2.display_info()

# Вызов метода __repr__
print(duck1)

# Сравнение уток по весу
print(duck1 > duck2)
print(duck1 < duck2)
print(duck1 == duck2)
print(duck1 != duck2)

# Использование метода __add__
combined_duck = duck1 + duck2
combined_duck.display_info()
