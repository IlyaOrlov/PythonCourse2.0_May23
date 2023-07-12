class Duck:
    color = "yellow"  # Общий атрибут цвет для всех экземпляров класса

    def __init__(self, name, weight):
        """
        Конструктор класса Duck.

        Args:
            name (str): Имя утки.
            weight (float): Вес утки.
        """
        self.name = name
        self.weight = weight

    @staticmethod
    def crack():
        """
        Статический метод выводящий звук треска утки.
        """
        print("Crack!")

    @classmethod
    def get_color(cls):
        """
        Классовый метод выводящий цвет уток.
        """
        print(f"Цвет уток {cls.color}.")

    def get_name(self):
        """
        Метод возвращающий имя утки.
        """
        return self.name

    def get_weight(self):
        """
        Метод возвращающий вес утки.
        """
        return self.weight

    def __lt__(self, other):
        """
        Метод сравнения текущей утки с другой по весу (<).

        Args:
            other (Duck): Другая утка для сравнения.

        Returns:
            bool: Результат сравнения.
        """
        return self.weight < other.weight

    def __eq__(self, other):
        """
        Метод сравнения текущей утки с другой по весу (==).

        Args:
            other (Duck): Другая утка для сравнения.

        Returns:
            bool: Результат сравнения.
        """
        return self.weight == other.weight

    def __gt__(self, other):
        """
        Метод сравнения текущей утки с другой по весу (>).

        Args:
            other (Duck): Другая утка для сравнения.

        Returns:
            bool: Результат сравнения.
        """
        return self.weight > other.weight

    def __ne__(self, other):
        """
        Метод сравнения текущей утки с другой по весу (!=).

        Args:
            other (Duck): Другая утка для сравнения.

        Returns:
            bool: Результат сравнения.
        """
        return self.weight != other.weight

    def __add__(self, other):
        """
        Метод сложения двух уток, возвращающий утку с суммарным весом.

        Args:
            other (Duck): Другая утка для сложения.

        Returns:
            Duck: Утка с суммарным весом.
        """
        total_weight = self.weight + other.weight
        return Duck("Сложение 2 уток", total_weight)

# Создание экземпляров уток
duck1 = Duck("Утка 1", 1.5)
duck2 = Duck("Утка 2", 2.0)

# Вызов статического метода
Duck.crack()  # Выводит: Crack!

# Вызов классового метода
Duck.get_color()  # Выводит: The color of ducks is yellow.

# Вызов методов экземпляров
print(duck1.get_name())  # Выводит: Утка 1
print(duck2.get_weight())  # Выводит: 2.0

# Примеры сравнения уток по весу
print(duck1 < duck2)  # Выводит: True
print(duck1 == duck2)  # Выводит: False
print(duck1 > duck2)  # Выводит: False
print(duck1 != duck2)  # Выводит: True

# Пример сложения уток
combined_duck = duck1 + duck2
print(combined_duck.get_name())  # Выводит: сложение
print(combined_duck.get_weight())  # Выводит: 3.5